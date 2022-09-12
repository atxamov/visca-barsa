from rest_framework import serializers
from home.models import Book
from home.models import Publisher
from home.models import Journalist
from home.models import Mananger
from home.models import NationalT


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
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