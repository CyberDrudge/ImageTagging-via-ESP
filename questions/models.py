from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

from .utilities import upload_image_path


# Create your models here.
class SecondaryImage(models.Model):
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)


class PrimaryImage(models.Model):
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    secondary_image = models.ManyToManyField(SecondaryImage, blank=True)
    consensus_reached = models.BooleanField(default=False)


class Selected(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(PrimaryImage, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.ManyToManyField(SecondaryImage, blank=True)
    is_active = models.BooleanField(default=True)


def check_consensus(*args, **kwargs):
    qs = PrimaryImage.objects.filter(consensus_reached=False)
    if not qs.exists():
        txt_ = "Hey Admin, Consensus has been reached for questions on your ESP Game. Please add more questions for the users."
        subject = 'Consensus Notification'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]
        sent_mail = send_mail(
            subject,
            txt_,
            from_email,
            recipient_list,
        )
        return sent_mail


# post_save.connect(check_consensus, sender=PrimaryImage)

