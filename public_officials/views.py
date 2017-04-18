from django.shortcuts import render, redirect
from django.http import HttpResponse
from public_officials.services import *
from public_officials.models import *
import json
import pdb

def home_page(request):
    return render(request, 'public-officials/home.html')

def legislator_detail(request, legislator_id):
    legislator_service = LegislatorService()
    legislator = Legislator.objects.get(pk=legislator_id)
    cid = legislator.cid
    organization_contributors = legislator_service.get_legislator_org_contributions(cid)
    industry_contributors = legislator_service.get_legislator_ind_contributions(cid)
    return render(request, 'public-officials/detail.html', {'legislator': legislator, 'organizations': organization_contributors, 'industries': industry_contributors})

def senator_index(request):
    senators = Legislator.objects.filter(chamber="senate")
    return render(request, 'public-officials/senators/index.html', {'senators': senators})

def representative_index(request):
    representatives = Legislator.objects.filter(chamber="house")
    return render(request, 'public-officials/representatives/index.html', {'representatives': representatives})
