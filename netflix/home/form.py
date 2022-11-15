from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Movie Name"}), label='')
    year = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Enter Year"}), label='')
    desc = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Description"}), label='')

    class Meta:
        model = Movie
        fields = '__all__'

        label = {
            "name": "",
        }
