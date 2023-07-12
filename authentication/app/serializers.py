from rest_framework import serializers
from .models import Book,User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class BookSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id','title', 'description', 'author', 'price']
