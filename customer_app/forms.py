from django import forms

from customer_app.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'temperament', 'health_status','photo']

ROOM_CHOICES = [
    ('standard', 'Standard'),
    ('deluxe', 'Deluxe'),
    ('premium', 'Premium'),
]

class BoardingForm(forms.ModelForm):
    room_preference = forms.ChoiceField(choices=ROOM_CHOICES)
    class Meta:
        model = Boarding
        fields = ['start_date', 'end_date', 'room_preference', 'special_requirements']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['description']