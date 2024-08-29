# from django.conf import settings
from rest_framework.filters import BaseFilterBackend


class GeocollectionPermissionsFilter(BaseFilterBackend):
    """
    A filter backend that limits results to those where the requesting user
    has read object-level permissions.
    """

    shortcut_kwargs = {
        "accept_global_perms": True,
    }

    def filter_queryset(self, request, queryset, view):
        # We want to defer this import until runtime, rather than import-time.
        # See https://github.com/encode/django-rest-framework/issues/4608
        # (Also see #1624 for why we need to make this import explicitly)
        from guardian.shortcuts import get_objects_for_user

        user = request.user

        obj_with_perms = get_objects_for_user(
            user, "geocollections.access_geocollection", **self.shortcut_kwargs
        )

        return queryset.filter(id__in=obj_with_perms.values("id"))
