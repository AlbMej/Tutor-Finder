'''
Description

This file contains the python
backend for every form with the webapp.
Forms are the most common way of getting
user input from the User Interface and
processing it into a database table
'''


from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.core.exceptions import ValidationError
from tutor_finder.core.models import UserInfo
from tutor_finder.core.models import Tutor
from tutor_finder.core.models import Ratings
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


# Form to display text/other submission widgets,
# and to gather form data, mirrored to a tutor model for
# easy db submission/storage
class InfoFieldForm(forms.ModelForm):
    class Meta:
        #tells the form what model to user from models.py
        model = UserInfo

        fields = ('first_name', 'last_name', 'phone_TB', 'email_TB', 'other_TB1'
                 , 'other_TB2', 'agree',
                 'school', 'level')

        LEVELS = (
                 ('' , 'Choose'),
                 ('Fr', 'Freshman'),
                 ('So', 'Sophmore'),
                 ('Jr', 'Junior'),
                 ('Sr', 'Senior'),
                 ('M', 'Masters'),
                 ('P', 'Phd')
                 )

        #for the text inputs, placeholder refers to example text in light gray
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex. John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex. Doe'}),
            'phone_TB': forms.TextInput(attrs={'placeholder': 'Ex. 518-867-5309'}),
            'email_TB': forms.TextInput(attrs={'placeholder': 'Ex. john.doe@example.com'}),
            'other_TB1': forms.TextInput(attrs={'placeholder': 'Ex. Twitter'}),
            'other_TB2': forms.TextInput(attrs={'placeholder': 'Ex. @JohnDoe'}),
            'school': forms.TextInput(attrs={'placeholder': 'Ex. RPI'})
        }

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

#this class goes with the "InfoFieldForm" above
class CustomFieldForm(InfoFieldForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].required = True
        self.helper = FormHelper()
        #the layout, row by row
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('phone_TB', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('email_TB', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('other_TB1', css_class='form-group col-md-5 mb-0'),
                Column('other_TB2', css_class='form-group col-md-7 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('school', css_class='form-group col-md-6 mb-0'),
                Column('level', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            CustomCheckbox('agree'),
            Submit('submit', 'Submit')
        )


# form to display tutor search bar, used to
# validate data, and foward to search results/filters
class TutorSearchForm(forms.Form):


    class_search = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' : 'Search for Tutor by Class!'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'class_search',
            Submit('submit','Search')
        )


class RatingForm(forms.Form):
    class Meta:
        model = Ratings

        fields = ('score', 'comment', 'tutor_id')

        #for the text inputs, placeholder refers to example text in light gray
        widgets = {
            'score': forms.NumberInput(attrs={'placeholder': '4'}),
            'comment': forms.TextInput(attrs={'placeholder': 'excellent with explaing the homework'}),
            'tutor_id': forms.NumberInput(attrs={'placeholder': 'This needs to be automatic'}),
        }

#this class goes with the "TutorListing" above
class RatingFormLayout(RatingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #the layout, row by row
        self.helper.layout = Layout(
            Row(
                Column('score', css_class='form-group col-md-4 mb-0'),
                Column('comment', css_class='form-group col-md-4 mb-0'),
                Column('tutor_id', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )

# form to display/capture search filter user filled data
# inherents from TutorSearchForm in order to bring along the
# general search bar and to provide the filtered form with
# access to the general search term
class TutorSearchFilterForm(TutorSearchForm):

    time = forms.DateTimeField(initial=datetime.datetime.today,required=False)
    max_price = forms.DecimalField(required=False)
    lowest_rating = forms.DecimalField(initial=0.0,required=False)
    school = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'School'}),required=False,empty_value=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'class_search',
            Row(
                Column('time',css_class='form-group col-md-6 mb-0'),
                Column('school',css_class='form-group col-md-6 mb-0'),
                css_class = 'form_row'
            ),
            Row(
                Column('max_price',css_class='form-group col-md-6 mb-0'),
                Column('lowest_rating',css_class='form-group col-md-6 mb-0'),
                css_class = 'form_row'
            ),
            Submit('submit','Apply Filters')
        )


class TutorListing(forms.ModelForm):
    class Meta:
        #tells the form what model to user from models.py
        model = Tutor

        fields = ('name', 'price', 'course', 'school')

        #for the text inputs, placeholder refers to example text in light gray
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Perferred name'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Ex. 15 (this is $/hr)'}),
            'course': forms.TextInput(attrs={'placeholder': 'Ex. Software Design and Documentation'}),
            'school': forms.TextInput(attrs={'placeholder': 'Ex. RPI'})
        }

#this class goes with the "TutorListing" above
class TutorListingForm(TutorListing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        #the layout, row by row
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-4 mb-0'),
                Column('price', css_class='form-group col-md-4 mb-0'),
                Column('school', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('course', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )
