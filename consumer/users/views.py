import httpx

from django.shortcuts import render
from django.http import HttpResponse


async def index(request):  # [1]
    async with httpx.AsyncClient() as client:  # [2]
        response = await client.get(
            "http://localhost:8000/users/users/", auth=("admin", "password")
        )  # [3]
    users = response.json()  # [4]
    return render(request, "users/index.html", {"users": users})  # [5]


# [1] This app does have views, but they're normal, asynchronous views.
# [2] It starts an asynchronous client request, that's why here we're using httpx.
# [3] Since it's asynchronous, we write await, then client and the address,
# plus authentication details.
# IMPORTANT: make sure to create a superuser before running this!
# [4] Once it has received the response (which will be just a text string), it
# will read that as JSON.
# [5] Finally, it'll make users part of the context and render it with a template
# (see users/index.html).
