from django import http
import httpx
from asgiref.sync import sync_to_async  # [6]

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings

# from django.views.decorators.cache import cache_page
from django.core.cache import cache


def get_local_users():  # [7]
    users = cache.get("users")
    if not users:
        users = list(User.objects.all())
        cache.set("users", users, 15)
    return users


async def index(request):
    context = {}
    remote_users = await cache.aget("remote_users")
    if remote_users:
        context["remote_users"] = remote_users
    else:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://localhost:8000/users/users",
                    headers={"Authorization": f"Token {settings.AUTH_TOKEN}"},
                )
            json = response.json()
            remote_users = json["results"]
            context["remote_users"] = remote_users
            await cache.aset("remote_users", remote_users, 15)
        except httpx.RequestError as exc:
            context["connection_error"] = True
    context["local_users"] = await sync_to_async(
        get_local_users, thread_sensitive=True
    )()
    return render(request, "users/index.html", context)


# OLD VERSION
# # @cache_page(60) # [9]
# async def index(request):  # [1]
#     context = {}
#     try:
#         async with httpx.AsyncClient() as client:  # [2]
#             response = await client.get(
#                 "http://localhost:8000/users/users/",
#                 headers={"Authorization": f"Token {settings.AUTH_TOKEN}"},
#             )  # [3]
#         json = response.json()  # [4]
#         context["remote_users"] = json["results"]
#     except httpx.RequestError as exc:
#         context["connection_error"] = True
#     context["local_users"] = await sync_to_async(
#         get_local_users, thread_sensitive=True
#     )()  # [8]
#     return render(request, "users/index.html", context)  # [5]


# [1] This app does have views, but they're normal, asynchronous views.
# [2] It starts an asynchronous client request, that's why here we're using httpx.
# [3] Since it's asynchronous, we write await, then client and the address,
# plus authentication details.
# IMPORTANT: make sure to create a superuser before running this!
# [4] Once it has received the response (which will be just a text string), it
# will read that as JSON.
# [5] Finally, it'll make users part of the context and render it with a template
# (see users/index.html).

# [6] A converter that makes having the synchronous inside the asynchronous possible.

# [7] A function that does all the things that have to be done synchronously. In this
# case, it'll return a list of all users.

# [8] This is a synchronous call.
# The "extra" set of parenthesis at the end of this line are there to call the
# asynchronous function, which doesn't take any arguments.

# [9] Only works for synchronous views, therefore we can't use it in this case.
