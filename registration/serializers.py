from random import random, randint
from rest_framework import serializers
from .models import HubreeUser

class HubreeUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = HubreeUser
        fields = ('userid', 'username', 'firstname', 'lastname', 'pincode', 'contact', 'email', 'password')



