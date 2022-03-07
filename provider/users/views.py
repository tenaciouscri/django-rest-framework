from django.contrib.auth.models import User, Group
from rest_framework import viewsets # [1]
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer



class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''

    queryset = User.objects.all().order_by("-date_joined") # [2]
    serializer_class = UserSerializer # [3]
    permission_classes = [permissions.IsAuthenticated] # [4]

class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited.
    '''

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# [1] Viewsets are a type of class-based view that is made specifically
# for the REST API. They have methods for how to deal with list, create,
# retrieve, update, partial_update, destroy.
# https://www.django-rest-framework.org/api-guide/viewsets/

# [2] Take all User objects and order them by most to least recent.

# [3] Which serializer class should it use?

# [4] Only authenticated users get access to this viewset.