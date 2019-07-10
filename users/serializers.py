from rest_framework.serializers import ModelSerializer
from .models import CustomerUser
from rest_framework.fields import ReadOnlyField


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['email', 'username','']

