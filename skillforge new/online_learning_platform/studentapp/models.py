from django.db import models
from django.utils import timezone

class UserCertificate(models.Model):
    full_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.course_name}"

