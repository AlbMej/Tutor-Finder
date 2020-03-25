from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .forms import CustomFieldForm, TutorSearchForm, TutorSearchFilterForm
from .models import Tutor






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
            years = form.cleaned_data['years_in_college']

            if amount > 25 and years < 1:
                return redirect("denied")
            elif amount < 25 and years >= 1:
                return redirect("preapproved")
            else:
                return redirect("success")

    else:
        form = CustomFieldForm()

    return render(request, "form.html", {
        'form': CustomFieldForm()
    })


class SearchView(TemplateView):
    template_name = 'tutor_search.html'


    def search_form(request):
        form = TutorSearchForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form = TutorSearchFilterForm(request.POST)
        else:
            form = TutorSearchForm()
        return render( request, 'tutor_search.html',{'form': form})
    
class SearchResultsView(ListView):
    model = Tutor
    template_name = 'tutor_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Tutor.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))

        return object_list
    # def get_name( request ):
    #     if request.method == 'GET' :
