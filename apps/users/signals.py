from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import Users, Students


@receiver(post_save, sender=Users)
def create_user(sender, instance, created, **kwargs):

    if created:
        Students.objects.create(students_profile=instance)