from django.urls import re_path as url

from .views import (
    GeocollectionDetail,
    geocollection_permissions,
)

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$',
        GeocollectionDetail.as_view(),
        name='geocollection-detail'),
    url(r'^permissions/(?P<collection_slug>[-\w]+)/$',
        geocollection_permissions,
        name='geocollection-permissions'),
]
