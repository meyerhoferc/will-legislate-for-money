from django.shortcuts import render, redirect
from django.http import HttpResponse
import pdb #pdb.set_trace()

def home_page(request):
    return render(request, 'public-officials/home.html')
