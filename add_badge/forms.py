from .models import Badge, BadgeRequirements
from django import forms
from django.forms import inlineformset_factory

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'description', 'category', 'image']


BadgeRequirementFormSet = inlineformset_factory(
    Badge,
    BadgeRequirements,
    fields=["text",],
    extra=1,
    can_delete=True
)
