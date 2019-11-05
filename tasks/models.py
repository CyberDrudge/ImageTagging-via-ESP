from django.db import models
from questions.models import PrimaryImage
from django.contrib.auth.models import User
from random import sample

task_size = 5


# Create your models here.
class TaskManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        qs = self.get_queryset().filter(is_active=True).exclude(user=user)
        new_obj = False
        if qs.count() >= 1:
            task_obj = qs.first()
            task_obj.user.add(user)
        else:
            new_obj = True
            task_obj = Task.objects.create()
            task_obj.user.add(user)
            questions = list(PrimaryImage.objects.all().values_list('id', flat=True))
            ques = sample(questions, task_size)
            task_obj.questions.set(ques)
        return task_obj, new_obj


class Task(models.Model):
    user = models.ManyToManyField(User, blank=True)
    questions = models.ManyToManyField(PrimaryImage, blank=True)
    is_active = models.BooleanField(default=True)

    objects = TaskManager()

