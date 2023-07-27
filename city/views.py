import os
import uuid
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework.filters import SearchFilter
from .models import City
from .serializers import CitySerializer
from django.conf import settings




class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by('-created_at')
    serializer_class = CitySerializer
    filter_backends = [SearchFilter]
    pagination_class = StandardResultsSetPagination
    search_fields = ['name']

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
            image_name = 'city_' + str(uuid.uuid4()) + '.jpg'
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
            city = serializer.instance
            if city.cover_image:
                dbcover_image = city.cover_image
                serializer.validated_data['cover_image'] = city.cover_image
            # Save the model instance
            serializer.save()
        else:
            city = serializer.instance
            dbcover_image = city.cover_image
            if city.cover_image:
                city.cover_image = None
                # Check if the image is stored
                if os.path.exists(dbcover_image.path):
                    # The image is not stored, so delete it from the database
                    os.remove(dbcover_image.path)
            # Get the image file from the request
            image_file = self.request.FILES['cover_image']
            # Rename the image file
            image_name = 'city_' + str(uuid.uuid4()) + '.jpg'
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



    def perform_destroy(self, instance):
        dbcover_image = instance.cover_image
        if instance.cover_image:
            # Check if the image is stored
            if os.path.exists(dbcover_image.path):
                # The image is not stored, so delete it from the database
                os.remove(dbcover_image.path)
        #self().perform_delete(instance)
        instance.delete()







