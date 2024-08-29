from math import ceil

from rest_framework import status
from rest_framework.decorators import api_view
from geonode.documents.models import Document
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.authorization import DjangoAuthorization
from guardian.shortcuts import get_objects_for_user
from geonode.api.api import ProfileResource, GroupResource
from geonode.api.resourcebase_api import ResourceBaseResource

from .models import Geocollection
from .serializers import BulletinListSerializer


class GeocollectionAuth(DjangoAuthorization):

    def read_list(self, object_list, bundle):
        permitted_ids = get_objects_for_user(
            bundle.request.user, "eswatini.access_geocollection"
        ).values("id")

        return object_list.filter(id__in=permitted_ids)

    def read_detail(self, object_list, bundle):
        return bundle.request.user.has_perm("access_geocollection", bundle.obj)


class GeocollectionResource(ModelResource):

    users = fields.ToManyField(
        ProfileResource,
        attribute=lambda bundle: bundle.obj.group.group.user_set.all(),
        full=True,
    )
    group = fields.ToOneField(GroupResource, "group__group", full=True)
    resources = fields.ToManyField(
        ResourceBaseResource, "resources", full=True
    )

    class Meta:
        queryset = Geocollection.objects.all().order_by("-group")
        ordering = ["group"]
        allowed_methods = ["get"]
        resource_name = "geocollections"
        filtering = {"group": ALL_WITH_RELATIONS, "id": ALL}


@api_view(["GET"])
def get_bulletin_list(request):
    paginator = PageNumberPagination()
    queryset = Document.objects.order_by("-created")
    instance = paginator.paginate_queryset(queryset, request)
    total = queryset.count()
    page_size = 10
    data = BulletinListSerializer(instance=instance).data
    return Response(
        {
            "current": int(request.GET.get("page", "1")),
            "total": total,
            "total_page": ceil(total / page_size),
            "data": data,
        },
        status=status.HTTP_200_OK,
    )
