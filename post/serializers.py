from rest_framework import serializers
from .models import PostUser

class PostSerializers(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'author.username')

    class Meta:
        model = PostUser
        fields = ['id','username','message']