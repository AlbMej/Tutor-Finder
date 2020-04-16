"""tutor_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Description:
This file contains a list of all the urls for
the website, changes to this file are necessary
for adding a new page to the webapp
"""
from django.contrib import admin
from django.urls import path, include
from tutor_finder.core import views
from django.conf.urls import include


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('submit_form', views.submit_form, name = 'tutorform'),
    path('create_listing', views.create_listing, name = 'create_listing'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('denied/', views.DeniedView.as_view(), name='denied'),
    path('preapproved/', views.PreapprovedView.as_view(), name='preapproved'),
    path('tutor_search/', views.SearchView.search_form, name = 'tutor_search'),
    path('tutor_search_results/', views.SearchResultsView.search_results, name = 'tutor_search_results'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls'))
]
