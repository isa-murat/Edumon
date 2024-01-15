from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import Users, Teachers, Students


@receiver(post_save, sender=Users)
def create_user(sender, instance, created, **kwargs):

    if created:
        if instance.user_type == 'teacher':
            Teachers.objects.create(teachers_profile=instance)
        elif instance.user_type == 'student':
            Students.objects.create(students_profile=instance)