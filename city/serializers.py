from rest_framework import serializers
from .models import City
from core.models import User


class CitySerializer(serializers.ModelSerializer):
   user_id = serializers.IntegerField(allow_null=True)
   class Meta:
      model = City
      fields = ['id', 'cover_image', 'name', 'description', 'user_id', 'created_at', 'updated_at']