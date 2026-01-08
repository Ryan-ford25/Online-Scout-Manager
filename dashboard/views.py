from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from add_badge.models import ScoutBadge, BadgeRequest, Badge

@login_required
def scout_dashboard(request):
    earned_badges = ScoutBadge.objects.filter( scout=request.user).select_related("badge")
    return render(request, 'dashboard/scout_dashboard.html', {'earned_badges': earned_badges})

@login_required
def home(request):
    return render(request, 'dashboard/default_dash.html')

@login_required
def leader_dashboard(request):
    requests = BadgeRequest.objects.filter(status="pending")
    return render(request, "dashboard/leader_dashboard.html", {"requests": requests})
