# housing/urls.py
# dir /housing

from django.conf.urls import url, include

from .views import housing, nothing_here

urlpatterns = [
	
	url(r'^$', housing),
	
	
	url(r'.*', nothing_here),
]
