from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from django.core.exceptions import ValidationError
from tutor_finder.core.models import UserInfo

class InfoFieldForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('first_name', 'last_name', 'email', 'phone',
                'address', 'city', 'state', 'zip_code', 'amount_required',
                'major', 'years_in_college', 'other', 'agree')

        MAJORS = (
                ('', 'Choose...'),
                ('CS', 'Computer Science'),
                ('EE', 'Electrical Engineering'),
                ('CHEM', 'Chemistry'),
                ('OTH', 'Other')
            )

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ex. Alberto'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ex. Mejia'}),
            'email': forms.TextInput(attrs={'placeholder': 'Ex. alberto@tutorfinder.com'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ex. 914 123 4567'}),
            'address': forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor, 1234 Main St'}),
            'city': forms.TextInput(attrs={'placeholder': 'Yonkers'}),
            'state': forms.TextInput(attrs={'placeholder': 'NY'}),
            'zip_code': forms.TextInput(attrs={'placeholder': '10701'}),
            'amount_required': forms.TextInput(attrs={'placeholder': '25'}),
            'years_in_college': forms.TextInput(attrs={'placeholder': '3'}),
            'other': forms.TextInput(attrs={'placeholder': 'N/A'})
        }

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

class CustomFieldForm(InfoFieldForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agree'].required = True
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),


            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-2 mb-0'),
                Column('state', css_class='form-group col-md-2 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('amount_required', css_class='form-group col-md-4 mb-0'),
                Column('major', css_class='form-group col-md-4 mb-0'),
                Column('other', css_class='form-group col-md-2 mb-0'),
                Column('years_in_college', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            CustomCheckbox('agree'),
            Submit('submit', 'Submit')
        )
