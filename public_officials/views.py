from django.shortcuts import render, redirect
from django.http import HttpResponse
from public_officials.services import *
from public_officials.models import *
import pdb

def home_page(request):
    legislator_service = LegislatorService()
    legislator_list = legislator_service.get_legislators_by_state()
    return render(request, 'public-officials/home.html', {'legislator_list': legislator_list})

def legislator_detail(request, legislator_id):
    return render(request, 'public-officials/detail.html')
