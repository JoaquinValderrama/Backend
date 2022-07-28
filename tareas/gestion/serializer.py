from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class pruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40)
    apellido = serializers.CharField(max_length=40)