'''
This file is designed as the controller
if viewing as the model-view-controller
pattern, all html files rendered here
and the data is POSTed here for text processing
'''

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .forms import CustomFieldForm, TutorSearchForm, TutorSearchFilterForm, TutorListing, TutorListingForm
from .models import Tutor, School, Course, UserInfo
from urllib.parse import urlencode
import datetime
from django.contrib.auth import login, authenticate
from tutor_finder.core.forms import SignUpForm
# Create your views here.

# Render home page view
# count fills out number of registered users
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


# Render signup page
# POST HTTP request fills form with valid
# data, saves to db via django model/db access API
# otherwise populates empty form for submission
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

# Render simple tutor signup success page
class SuccessView(TemplateView):
    template_name = 'success.html'

# Render simple tutor signup denial page
class DeniedView(TemplateView):
    template_name = 'denied.html'

# Render preapproval tutor page
class PreapprovedView(TemplateView):
    template_name = 'preapproved.html'

# If user is logged in
# GET request renders empty Tutor Signup form
# POST request saves valid form data to DB, verifies
# a valid tutor signup, performs redirect as needed based on verification
# If user is NOT logged in:
# denies access, redirect to login
@login_required
def submit_form(request):
    form = CustomFieldForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user_ID = request.user
            temp.save()

    else:
        form = CustomFieldForm()

    return render(request, "form.html", {
        'form': CustomFieldForm()
    })

# If user is logged in
# GET request renders empty Tutor Listing form
# POST request saves valid form data to DB
# If user is NOT logged in:
# denies access, redirect to login
@login_required
def create_listing(request):
    form = TutorListingForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            temp = form.save(commit=False)
            temp.user_ID = request.user
            temp.save()

    else:
        form = TutorListingForm()

    return render( request, "form.html" , {
        'form' : TutorListingForm()
        }
    )

# renders tutor search form
# only responsible for rendering the single search bar
# with no filters
# GET renders a blank search bar
# POST forwards the search term to a results/filter template form
# @SearchResultsView via POST request via DJANGO redirect API
class SearchView(TemplateView):
    template_name = 'tutor_search.html'

    def search_form(request):
        form = TutorSearchFilterForm(request.POST)
        html = 'tutor_search.html'

        if request.method == 'POST':
            if form.is_valid():
                #insert get response with search results for the next page
                #export as get variable somehow? from form
                html = reverse('tutor_search_results')
                query_string =  urlencode(request.POST)  # 2 category=42
                url = '{}?{}'.format(html, query_string)
                return redirect(url)
        else:
            form = TutorSearchForm()
        return render( request, html ,{'form': form})


# accepts requests from @SearchView
# a POST request querys the DB given the search
# term and given filters (if any) via the Django db/model API
# renders given results in a list
# A GET renders empty form

class SearchResultsView(ListView):
    ### Applies search to DB given valid form data
    def tut_search(query_set,method):
        class_search = query_set.cleaned_data['class_search']
        time_av = None
        max_price = None
        lowest_rating = None
        school = None
        start_t = None

        if method == 'POST':
            max_price = query_set.cleaned_data['max_price']
            lowest_rating = query_set.cleaned_data['lowest_rating']
            school = query_set.cleaned_data['school']
            start_t = query_set.cleaned_data['time']

        # this is where we query the db and return the list of tutor objects
        # we can figure out how to link the tutor results to actual pages later
        # prolly through some url nonsense, or a view/redirect href html thing
        tutor_query = Tutor.objects.filter(course__icontains=class_search)

        if school != None:
            tutor_query = tutor_query.filter(school__icontains=school)
        if max_price != None:
            tutor_query = tutor_query.filter(price__lte=max_price)
        if start_t != None:
            tutor_query = tutor_query.filter(start__lte=start_t)
            tutor_query = tutor_query.filter(end__gte=start_t)
            # else:
            #     tutor_query = tutor_query.filter(start=query_set.cleaned_data['start'])

        if(tutor_query.count() > 0):
            for tutor in tutor_query:
                User_Info = UserInfo.objects.filter(user_ID__icontains=tutor.user_ID)
        else:
            User_Info = []
        return (tutor_query, User_Info)

    ### Handles search form submission, validates submission data, Django parses
    ### into a neatly made list, submitted to query function
    def search_results(request):
        tutors = None
        print(request)
        form = TutorSearchFilterForm(request.POST)
        html = 'tutor_search_results.html'
        print(form.data)
        if request.method == 'POST':

            if form.is_valid():
                (tutors, users) = SearchResultsView.tut_search(form, 'POST')

        else:
            form = TutorSearchForm(request.GET)

            if form.is_valid():

                (tutors, users) = SearchResultsView.tut_search(form,'GET')
            form = TutorSearchFilterForm(request.GET)
        return render( request, html ,{
            'form' : form,
            'tutors' : tutors,
            'users' : users
            })
