from django.shortcuts import render
from django.views import generic
from .models import Badge, BadgeRequest, BadgeRequirements, ScoutBadge
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

class BadgeList(generic.ListView):
    queryset = Badge.objects.all()
    template_name = "badge_list.html"
    context_object_name = 'badges'


@login_required
def request_badge(request, badge_id):
    badge = get_object_or_404(Badge, id=badge_id)

    BadgeRequest.objects.get_or_create(
        scout=request.user,
        badge=badge
    )

    return redirect("dashboard:scout")

@login_required
def approve_badge_request(request, request_id):
    badge_request = get_object_or_404(BadgeRequest, id=request_id)
    badge_request.approve()
    return redirect("dashboard:leader")

@login_required
def reject_badge_request(request, request_id):
    badge_request = get_object_or_404(BadgeRequest, id=request_id)
    badge_request.reject()

    return redirect("dashboard:leader")

