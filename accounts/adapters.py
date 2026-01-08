from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAccountAdapter(DefaultAccountAdapter):
    
    def get_login_redirect_url(self, request):
        user = request.user


        profile = user.profile
        
        if profile.role == "scout":
            return reverse('dashboard:scout')

        if profile.role == "leader":
            return reverse('dashboard:leader')
        
        return reverse('dashboard:home')
