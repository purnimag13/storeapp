# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to the Blue Harvest Organic Grocery Store!")