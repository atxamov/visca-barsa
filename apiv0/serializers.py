from rest_framework import serializers
from home.models import *

class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'


class JournalistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Journalist
        fields = '__all__'


class ManangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mananger
        fields = '__all__'



class NationalTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NationalT
        fields = '__all__'


from django.contrib.auth.models import Group
class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class LoadDataExcel(serializers.BaseSerializer):
    file = serializers.FileField()