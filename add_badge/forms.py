from .models import Badge, BadgeRequirements
from django.forms import inlineformset_factory
from django import forms

class BadgeForm(forms.ModelForm):
    class Meta:
        model = Badge
        fields = ['name', 'description', 'category', 'image']

# Inline formset for requirements
BadgeRequirementFormSet = inlineformset_factory(
    Badge,                   # parent model
    BadgeRequirements,       # child model
    fields=['text',], # fields to include
    extra=5,                  # how many blank forms to show initially
    can_delete=True           # allow deleting a requirement
)