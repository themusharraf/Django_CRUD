from django import forms
from apps.models import Person,Job

class PersonForm(forms.ModelForm):
    job = forms.ModelChoiceField(Job.objects.all(), empty_label=None, required=True, to_field_name='name')

    class Meta:
        model = Person
        fields = '__all__'