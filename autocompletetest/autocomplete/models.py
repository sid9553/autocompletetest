from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from dal import autocomplete

# Create your models here.
class Step(models.Model):
	name = models.CharField(max_length = 100, default = '')
	def __unicode__(self):
		return (self.name)

class StepOption(models.Model):
	name = models.CharField(_('Step Option'), max_length = 100, default ='')
	step = models.ForeignKey(Step, related_name='Step', null=True)
	def __unicode__(self):
		return (self.name) or default

class RouteStep(models.Model):
	part_request_number = models.CharField(_('Part Request Number'),max_length=10, default = '')
	order = models.PositiveIntegerField(_('Step Number'), default = '')
	step = models.ForeignKey(Step, related_name='Step+', null=True)
	step_option = models.ForeignKey(StepOption, related_name = 'Option', null=True)
	performed = models.NullBooleanField(_('Complete'))
 	slug = models.SlugField(unique=False, null=True)
	def __unicode__(self):
		return (self.part_request_number)	