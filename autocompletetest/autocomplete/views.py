from django.shortcuts import render, redirect
from dal import autocomplete
from django.forms import formset_factory
from .models import Step, StepOption, RouteStep
from .forms import StepForm, StepOptionForm, RouteStepForm
# Create your views here.
class StepAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Step.objects.none()

        qs = Step.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
	
class StepOptionAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return StepOption.objects.none()

	s = StepOption.objects.all()
	step = self.forwarded.get('step', None)
        if step:
            s = s.filter(step=step)
        if self.q:
            s = s.filter(name__istartswith=self.q)
        return s


def autocompletetest(request):
	RouteStepFormSet = formset_factory(RouteStepForm, can_delete=False)
	if request.method == 'POST':
		formset = RouteStepFormSet(request.POST, request.FILES)
		if formset.is_valid():
			for form in formset.forms:
				formset.save()
			return redirect("http://127.0.0.1:8000/")
	else: 
		formset = RouteStepFormSet()
	return render(request, "autocomplete/autocompletetest.html", {'formset' :formset})