from rest_framework import serializers
from .models import *

class StundentSerializers(serializers.Serializer):
    name=serializers.CharField( max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField( max_length=50)
