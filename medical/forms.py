from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'age', 'bio']
        exclude = ['user']

class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['disease_diagnosed', 'disease_treatment', 'age_diagnosed', 'lab_results', 'recurrency']
        exclude = ['user']