from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter() # [3]
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)), # [2]
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")) # [1]
]

# [1] This url is needed for the REST framework browsable API to work. A browsable API
# is aimed at end users, so that we can take a look at it (for development purposes)
# to see how it works. It is something that comes with DRF.
# To look at it: go in the project folder, run server, open browser to the main url.
# Here, you'll be able to understand and see what's accessible. In this case, if we
# access http://127.0.0.1:8000/users/ we can see that from GET /users/ we can go into
# the users part and the groups part. By default, it returns JSON (see example below).
# IMPORTANT: Don't forget to login first, otherwise you won't be able to see the lists!
# NOTE: You can access the API from the command-line as well (provided that the server
# is running) with the following command:
# curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/users/users/
#
# --- EXAMPLE OF LIST --- 
# {
#     "count": 2, <- the number of users
#     "next": null, <- next results
#     "previous": null, <- previous results
#     "results": [
#         {
#             "url": "http://127.0.0.1:8000/users/users/2/",
#             "username": "user",
#             "email": "user@user.com",
#             "groups": []
#         },
#         {
#             "url": "http://127.0.0.1:8000/users/users/1/",
#             "username": "admin",
#             "email": "admin@admin.com",
#             "groups": []
#         }
#     ]
# }
# https://www.django-rest-framework.org/topics/browsable-api/

# [2] REST Framework comes with its own router system.
# [3] First, you create a router.
# [4] Then, you register an url for each view, specifying the Viewset.
# All these then get linked to the main path [2].

# At this point, we have a basic API that shows the list of users and groups.