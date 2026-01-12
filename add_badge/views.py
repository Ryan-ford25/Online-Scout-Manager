from django.shortcuts import render
from django.views import generic
from .models import Badge, BadgeRequest, BadgeRequirements, ScoutBadge
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
# Create your views here.

class BadgeList(generic.ListView):
    queryset = Badge.objects.all()
    template_name = "badge_list.html"
    context_object_name = 'badges'

@login_required
def request_badge(request, badge_id):
    badge = get_object_or_404(Badge, id=badge_id)

    badge_request, created = BadgeRequest.objects.get_or_create(
        scout=request.user,
        badge=badge
    )

    if not created and badge_request.status == "rejected":
        badge_request.status = "pending"
        badge_request.save(update_fields=["status"])

    messages.add_message(
        request, messages.SUCCESS, 'Badge request submitted.'
        )
    return redirect("badge_detail", slug=badge.slug)

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


def badge_detail(request, slug):
    badge = get_object_or_404(Badge, slug=slug)
    requirements = badge.requirements.all()

    has_badge = False
    has_pending_request = False

    if request.user.is_authenticated:
        has_badge = ScoutBadge.objects.filter( 
            scout=request.user,
            badge=badge
        ).exists()
        
        has_pending_request = BadgeRequest.objects.filter(
            scout=request.user,
            badge=badge,
            status="pending"
        ).exists()

    return render(
        request,
        "add_badge/badge_detail.html",
        {
            "badge": badge,
            "requirements":requirements,
            'has_badge': has_badge,
            "has_pending_request": has_pending_request,
        },
    )
