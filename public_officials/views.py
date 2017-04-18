from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from public_officials.services import *
from public_officials.models import *
import json
import pdb

def home_page(request):
    states = Legislator.get_all_state_names()
    return render(request, 'public-officials/home.html', {'states': states})

def legislator_detail(request, legislator_id):
    legislator_service = LegislatorService()
    legislator = Legislator.objects.get(pk=legislator_id)
    cid = legislator.cid
    organization_contributors = legislator_service.get_legislator_org_contributions(cid)
    return render(request, 'public-officials/detail.html', {'legislator': legislator, 'organizations': organization_contributors})

def senator_index(request):
    senators_by_state = Legislator.get_senators_by_state()
    return render(request, 'public-officials/senators/index.html', {'senators_by_state': senators_by_state, 'states': senators_by_state.keys()})

def representative_index(request):
    representatives_by_state = Legislator.get_representatives_by_state()
    return render(request, 'public-officials/representatives/index.html', {'representatives_by_state': representatives_by_state, 'states': representatives_by_state.keys()})

def industry_contributions(request):
    legislator_id = request.GET['legislator_id']
    legislator_service = LegislatorService()
    industry_contributors = legislator_service.get_legislator_ind_contributions(legislator_id)
    return render_to_response('public-officials/detail.html', {'industries': industry_contributors})
