from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Patrols, Profile
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


@login_required
def scout_list(request):
    scouts = Profile.objects.filter(role="scout").select_related("user")
    patrols = Patrols.objects.all()

    return render(request, "accounts/scout_list.html", {
        "scouts":scouts,
        "patrols":patrols,
    })

@login_required
def assign_patrol(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    patrol_id = request.POST.get("patrol")
    if patrol_id:
        profile.patrol = Patrols.objects.get(id=patrol_id)
    else:
        profile.patrol = None

    profile.save()
    return redirect("scout_list")
