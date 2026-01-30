from allauth.account.forms import SignupForm
from django import forms


class NewSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label="Last Name")
    ROLE_CHOICES = [
        ('scout', 'Scout'),
        ('leader', 'Leader'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Role')

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        from accounts.models import Profile
        Profile.objects.create(user=user, role=self.cleaned_data['role'])
        return user
