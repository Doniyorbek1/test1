from rest_framework import serializers
from api.models import User, Test, Result
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    


        