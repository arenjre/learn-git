from unicodedata import name
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.Serializer):
    name=serializers.CharField()
    publish_date = serializers.DateTimeField()
    author=serializers.CharField()
    
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self , b,  validated_data):
        newbook=Book(**validated_data)
        newbook.id=b.id;
        newbook.save()
        return newbook
    
class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=30)
    email=serializers.CharField(max_length=40)
    password=serializers.CharField(max_length=100)
    first_name=serializers.CharField(max_length=100)
    
class CourseSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    author=serializers.CharField(max_length=200)
    price=serializers.IntegerField()
    doscount=serializers.IntegerField(default=0)
    duration=serializers.FloatField()
    
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
        
        

    


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Review
        fields = (
            'url', 'author', 'professor',
            'created', 'updated', 'rating', 'text'
        )    