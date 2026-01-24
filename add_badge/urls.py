from . import views
from django.urls import path

urlpatterns = [
    path('badges/', views.BadgeList.as_view(), name = 'badges'),
    path("request/<int:badge_id>", views.request_badge, name="request_badge"),
    path("approve/<int:request_id>", views.approve_badge_request, name="approve_badge_request"),
    path("reject/<int:request_id>", views.reject_badge_request, name="reject_badge_request"),
    path("badge/<slug:slug>", views.badge_detail, name = "badge_detail"),
    path("badges/add", views.add_badge, name = "add_badge"),
    path('badges/<int:badge_id>/edit', views.edit_badge, name='edit_badge'),
    path("badges/delete/<int:badge_id>", views.delete_badge, name="delete_badge"),
    path("featured_badge/<int:scout_badge_id>", views.featured_badges,name="featured_badge" ),
]