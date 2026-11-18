from django import forms

from .models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "age", "department", "email", "phone_number", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 4}),
        }
