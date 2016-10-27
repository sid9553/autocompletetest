from django import forms
from .models import Step, StepOption, RouteStep
from dal import autocomplete

class StepForm(forms.ModelForm):

	class Meta:
		model = Step
		fields = '__all__'

class StepOptionForm(forms.ModelForm):

	class Meta:
		model = StepOption
		fields = '__all__'

		widgets = {
            'step': autocomplete.ModelSelect2(url='stepautocomplete')
        }

class RouteStepForm(forms.ModelForm):

	class Meta:
		model = RouteStep
		fields = '__all__'
		readonly_fields = 'part_request_number'
		exclude = ['part_request_number', 'slug']

		widgets = {
			'step': autocomplete.ModelSelect2(url='stepautocomplete'),
			'step_option': autocomplete.ModelSelect2(url='stepoptionautocomplete', forward=['step'])
        }

		