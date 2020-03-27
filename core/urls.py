# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin, sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include  # add this

from corona.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}


urlpatterns = [
    path("", include("corona.urls")),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
    # path("", include("authentication.urls")),  # add this
    # path("", include("app.urls"))  # add this
]
