import os
import uuid
import datetime
import random
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from .models import City
from .serializers import CitySerializer
from django.conf import settings




class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_create(self, serializer): 
        if 'cover_image' not in self.request.FILES:
            name = self.request.data['name']
            description = self.request.data['description']
            user_id = self.request.data['user_id']
            # Get the serializer with the data
            serializer.validated_data['name'] = name
            serializer.validated_data['description'] = description
            serializer.validated_data['user_id'] = user_id
            # Save the model instance
            serializer.save()
        else:
            # Get the image file from the request
            image_file = self.request.FILES['cover_image']
            # Rename the image file
            image_name = 'image_' + str(uuid.uuid4()) + '.jpg'
            # Save the image file to the media directory
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)
            with open(image_path, 'wb') as f:
                f.write(image_file.read())
            # Get the serializer with the image data
            serializer.validated_data['cover_image'] = image_name
            name = self.request.data['name']
            description = self.request.data['description']
            user_id = self.request.data['user_id']
            # Get the serializer with the data
            serializer.validated_data['name'] = name
            serializer.validated_data['description'] = description
            serializer.validated_data['user_id'] = user_id
            # Save the model instance
            serializer.save()


    def perform_update(self, serializer): 
        if 'cover_image' not in self.request.FILES:
            name = self.request.data['name']
            description = self.request.data['description']
            user_id = self.request.data['user_id']
            # Get the serializer with the data
            serializer.validated_data['name'] = name
            serializer.validated_data['description'] = description
            serializer.validated_data['user_id'] = user_id
            # Save the model instance
            serializer.save()
        else:
            city = serializer.instance
            dbcover_image = city.cover_image
            if city.cover_image:
                city.cover_image = None
                # Check if the image is stored
                if dbcover_image.storage.exists(dbcover_image):
                    # The image is not stored, so delete it from the database
                    os.remove(dbcover_image)
            # Get the image file from the request
            image_file = self.request.FILES['cover_image']
            # Rename the image file
            image_name = 'image_' + str(uuid.uuid4()) + '.jpg'
            # Save the image file to the media directory
            image_path = os.path.join(settings.MEDIA_ROOT, image_name)
            with open(image_path, 'wb') as f:
                f.write(image_file.read())
            # Get the serializer with the image data
            serializer.validated_data['cover_image'] = image_name
            name = self.request.data['name']
            description = self.request.data['description']
            user_id = self.request.data['user_id']
            # Get the serializer with the data
            serializer.validated_data['name'] = name
            serializer.validated_data['description'] = description
            serializer.validated_data['user_id'] = user_id
            # Save the model instance
            serializer.save()

