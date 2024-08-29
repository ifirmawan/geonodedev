from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse

from rest_framework import serializers
from dynamic_rest.serializers import DynamicModelSerializer

from geonode.documents.models import Document
from .models import Geocollection


class GeocollectionSerializer(DynamicModelSerializer):

    class Meta:
        model = Geocollection
        name = "geocollection"
        fields = ("pk", "name", "group", "resources")


class BulletinListSerializer(DynamicModelSerializer):

    class Meta:
        model = Document
        name = "documents"
        fields = (
            "uuid", "title", "files", "doc_url", "thumbnail_url", "created"
        )
