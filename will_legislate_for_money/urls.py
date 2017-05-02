"""will_legislate_for_money URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from public_officials import views as public_official_views

urlpatterns = [
    url(r'^$', public_official_views.home_page, name="home"),
    url(r'^about/$', public_official_views.about, name="about"),
    url(r'^state/$', public_official_views.state_legislators, name="state"),
    url(r'^senators/$', public_official_views.senator_index, name="senator_index"),
    url(r'^representatives/$', public_official_views.representative_index, name="representative_index"),
    url(r'^recent-bills/$', public_official_views.bills_index, name="bills_index"),
    url(r'^legislators/', include('public_officials.urls')),
    url(r'^admin/', admin.site.urls),
]
