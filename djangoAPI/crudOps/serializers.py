from rest_framework import serializers
from crudOps.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('username','email','password')

