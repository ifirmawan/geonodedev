# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from django.conf.urls import include
from django.urls import re_path as url
from geonode.urls import urlpatterns
from geonode.api.urls import api
from geonode.api.urls import router

from eswatini.api import GeocollectionResource
from eswatini.views import get_about_view
from eswatini.views import GeocollectionViewSet, BulletinViewSet

api.register(GeocollectionResource())
router.register(r"geocollections", GeocollectionViewSet, "geocollections")
router.register(r"bulletins", BulletinViewSet, "bulletins")

# You can register your own urlpatterns here
urlpatterns += [
    url(r"", include(api.urls)),
    url(r"^api/v2/", include(router.urls)),
    url(r"^geocollections/", include("eswatini.urls")),
    url(r"^about-us/", get_about_view, name="eswatini-about-us"),
]
