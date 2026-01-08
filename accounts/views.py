from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

@login_required
def signup_redirect(request):
    profile = request.user.profile

    if profile.role == "scout":
        return redirect("dashboard:scout")

    if profile.role == "leader":
        return redirect("dashboard:leader")