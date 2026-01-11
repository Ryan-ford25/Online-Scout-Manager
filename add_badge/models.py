from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length = 200, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    image = CloudinaryField("image")

    def __str__(self):
        return f"{self.name} badge"


class BadgeRequirements(models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name = "requirements")
    description = models.CharField(max_length = 255)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.badge.name} - Requirement {self.order}"
    
    class Meta:
        ordering = ["order"]

class BadgeRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    scout = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="badge_requests"
    )
    badge = models.ForeignKey(
        "add_badge.Badge",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def approve(self):
        if self.status == "approved":
            self.save(update_fields = ["status"])
            return

        ScoutBadge.objects.get_or_create(
            scout = self.scout,
            badge = self.badge
        )

    def reject(self):
        if self.status == "rejected":
            return
        
        self.status = "rejected"
        self.save(update_fields=["status"])

    def __str__(self):
        return f"{self.scout.username} → {self.badge.name}"
    
class ScoutBadge(models.Model):
    scout = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey("Badge", on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("scout", "badge")

    def __str__(self):
        return f"{self.scout.username} - {self.badge.name}"