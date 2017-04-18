from django.conf.urls import url
from . import views

app_name = 'public_officials'
urlpatterns = [
    url(r'^industry-contributions/$', views.industry_contributions, name="industry"),
    url(r'^(?P<legislator_id>[0-9]+)/$', views.legislator_detail, name="detail"),
]
