from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

class SuccessView(TemplateView):
    template_name = 'success.html'


class DeniedView(TemplateView):
    template_name = 'denied.html'


class PreapprovedView(TemplateView):
    template_name = 'preapproved.html'


@login_required
def submit_form(request):
    form = CustomFieldForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            amount = form.cleaned_data['amount_required']
            years = form.cleaned_data['years_in_business']

            if amount > 50000 and years < 1:
                return redirect("denied")
            elif amount < 50000 and years >= 1:
                return redirect("preapproved")
            else:
                return redirect("success")

    else:
        form = CustomFieldForm()

    return render(request, "form.html", {
        'form': CustomFieldForm()
    })