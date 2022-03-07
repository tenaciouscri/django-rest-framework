from django.contrib.auth.models import User, Group # [3]
from rest_framework import serializers # [1]


class UserSerializer(serializers.HyperlinkedModelSerializer): # [2]
    class Meta:
        model = User # [4]
        fields = ["url", "username", "email", "group"] # [5]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

# [1] Serializers are something specific to Django Rest Framework.
# It's a description of how it should translate a model into the output
# that the REST API returns.
# e.g. how should it treat each field, how should it treat foreign keys, etc.
# https://www.django-rest-framework.org/api-guide/serializers/

# [2] There are different types of serializers, but one of the most commonly used
# is 'HyperlinkedModelSerializer'.

# [3] Since we don't have models of our own in this app, we use models that are
# already provided with the default Django installation (in this case, User and
# Group). 

# [4] Which model is the serializer using?

# [5] Which fields should be serialized?