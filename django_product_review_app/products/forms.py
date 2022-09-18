from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }