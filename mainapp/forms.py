from django import forms
from .models import *


class RecruitsForm(forms.ModelForm):
	class Meta:
		model = Recruit
		fields = ['name', 'living_planet', 'age', 'email']
	
	def __init__(self, *args, **kwargs):
		super(RecruitsForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'
	
	def clean_age(self):
		data = self.cleaned_data['age']
		if data < 18:
			raise forms.ValidationError('Тебе нет даже 18 лет. Повзрослей и, может быть, ты передумаешь!')
		return data

