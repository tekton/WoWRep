from django import forms

class CharacterImportAPIForm(forms.Form):
    name = forms.CharField()
	realm = forms.CharField()