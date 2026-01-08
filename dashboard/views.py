from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from add_badge.models import Badge, BadgeRequest

@login_required
def scout_dashboard(request):
    return render(request, 'dashboard/scout_dashboard.html')


@login_required
def leader_dashboard(request):
    return render(request, 'dashboard/leader_dashboard.html')


@login_required
def home(request):
    return render(request, 'dashboard/default_dash.html')

@login_required
def leader_dashboard(request):
    requests = BadgeRequest.objects.filter(status="pending")
    return render(request, "dashboard/leader_dashboard.html", {"requests": requests})
