from dal import autocomplete
from django.conf.urls import url
from django.contrib import admin
from autocomplete import views
from .models import RouteStep, Step  
from .views import StepAutoComplete, StepOptionAutoComplete

urlpatterns = [
	url(r'^autocompletetest/$', views.autocompletetest, name='autocompletetest'),	
	url(r'^stepautocomplete/$', StepAutoComplete.as_view(), name='stepautocomplete'),
    url(r'^stepoptionautocomplete/$', StepOptionAutoComplete.as_view(), name='stepoptionautocomplete'),
]
