from django import forms
from .models import InterviewFeedback

class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewFeedback
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
