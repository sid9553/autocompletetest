from django.contrib import admin
from django.db import models
from django import forms
from .models import Step, StepOption, RouteStep
from .forms import RouteStepForm, StepForm, StepOptionForm
# Register your models here.
admin.site.register(Step)
admin.site.register(StepOption)
admin.site.register(RouteStep)