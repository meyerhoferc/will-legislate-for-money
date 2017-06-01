from django.contrib.auth import logout
from django.contrib.auth.decorators import *
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from public_officials.services import *
from public_officials.models import *
from nvd3 import pieChart
from django.views.decorators.csrf import csrf_exempt
import json

def home_page(request):
    states = Legislator.get_all_state_names()
    return render(request, 'public-officials/home.html', {'states': states})

def legislator_detail(request, legislator_id):
    legislator = Legislator.objects.get(pk=legislator_id)
    following = request.user in legislator.users.all()
    return render(request, 'public-officials/detail.html', {'legislator': legislator, 'following': following})

def senator_index(request):
    senators_by_state = Legislator.get_senators_by_state()
    return render(request, 'public-officials/senators/index.html', {'senators_by_state': senators_by_state, 'states': senators_by_state.keys()})

def representative_index(request):
    representatives_by_state = Legislator.get_representatives_by_state()
    return render(request, 'public-officials/representatives/index.html', {'representatives_by_state': representatives_by_state, 'states': representatives_by_state.keys()})

def industry_contributions(request):
    legislator_id = request.GET['legislator_id']
    cache_key = 'industry_contributions_%s' % legislator_id
    cache_time = 86400
    industry_contributors = cache.get(cache_key)

    if not industry_contributors:

        if legislator_id != '':
            legislator_service = LegislatorService()
            industry_contributors = legislator_service.get_legislator_ind_contributions(legislator_id)
        else:
            industry_contributors = "empty"

        cache.set(cache_key, industry_contributors, cache_time)

    return JsonResponse(industry_contributors, safe=False)

def organization_contributions(request):
    legislator_id = request.GET['legislator_id']
    cache_key = 'organization_contributions_%s' % legislator_id
    cache_time = 86400
    organization_contributors = cache.get(cache_key)

    if not organization_contributors:

        if legislator_id != '':
            legislator_service = LegislatorService()
            organization_contributors = legislator_service.get_legislator_org_contributions(legislator_id)
        else:
            organization_contributors = "empty"

        cache.set(cache_key, organization_contributors, cache_time)

    return JsonResponse(organization_contributors, safe=False)

def sponsored_bills(request):
    legislator_id = request.GET['legislator_id']
    cache_key = 'sponsored_bills_%s' % legislator_id
    cache_time = 86400
    sponsored_bills = cache.get(cache_key)

    if not sponsored_bills:
        legislator_service = LegislatorService()
        sponsored_bills = legislator_service.get_recent_bills(legislator_id)
        cache.set(cache_key, sponsored_bills, cache_time)

    if len(sponsored_bills) == 0:
        sponsored_bills = "empty"

    return JsonResponse(sponsored_bills, safe=False)

def voting_history(request):
    legislator_id = request.GET['legislator_id']
    cache_key = 'voting_history_%s' % legislator_id
    cache_time = 43200
    voting_history = cache.get(cache_key)

    if not voting_history:
        legislator_service = LegislatorService()
        voting_history = legislator_service.get_voting_history(legislator_id)
        cache.set(cache_key, voting_history, cache_time)

    return JsonResponse(voting_history, safe=False)

def state_legislators(request):
    state = request.GET['state']
    senators = Legislator.objects.filter(state_name=state).filter(chamber="senate")
    representatives = Legislator.objects.filter(state_name=state).filter(chamber="house")
    return render(request, 'public-officials/state.html', {'state': state, 'senators': senators, 'representatives': representatives})

def bills_index(request):
    cache_key = 'recent_bills'
    cache_time = 1800
    bills = cache.get(cache_key)

    if not bills:
        bill_service = BillService()
        bills = bill_service.get_recent_bills()
        cache.set(cache_key, bills, cache_time)

    return render(request, 'public-officials/bills/index.html', {'bills': bills})

def about(request):
    return render(request, 'public-officials/about.html')

def log_out(request):
    logout(request)
    return redirect('/')

@login_required
def user_show(request):
    legislators = request.user.legislator_set.all()
    return render(request, 'public-officials/user_show.html', {'legislators': legislators})

@csrf_exempt
def add_follower(request):
    legislator_id = request.POST.get('lid')
    user_id = request.POST.get('uid')
    Legislator.objects.get(id=legislator_id).users.add(User.objects.get(id=user_id))
    return HttpResponse(status=200)

@csrf_exempt
def remove_follower(request):
    legislator_id = request.POST.get('lid')
    user_id = request.POST.get('uid')
    User.objects.get(id=user_id).legislator_set.remove(Legislator.objects.get(id=legislator_id))
    return HttpResponse(status=200)
