# -*- coding: utf-8 -*-
"""Views handler."""

from __future__ import unicode_literals
from django.shortcuts import render
from Locations.models import Location


def test_page(request):
	to_show = Location.objects.all
	return render(request, 'test.html', context={'to_show': to_show})