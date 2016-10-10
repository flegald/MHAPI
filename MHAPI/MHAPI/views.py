# -*- coding: utf-8 -*-
"""Views handler."""

from __future__ import unicode_literals
from django.shortcuts import render
from Locations.models import Location


def show_image(request, *args, **kwargs):
    """Display image."""
    filter_by = kwargs['map_img']
    get_img = Location.objects.filter(map_img=filter_by)
    map_img = get_img[0].map_img.path

    return render(request, 'img.html', context={'map_img': map_img})


def landing(request):
    """Show landing page."""
    return render(request, 'index.html')
