from django import forms
from django.forms import ModelForm

from .models import *

class PollForm(forms.ModelForm):

	class Meta:
		model = Poll
		fields = '__all__'