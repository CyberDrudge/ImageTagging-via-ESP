from django.conf import settings

from accounts.models import Player
from questions.models import Selected

user_limit = settings.CONSENSUS_NUMBER


def check_submission(request, task_obj):
    curr_user = request.user
    if task_obj.user.count() == user_limit:
        score = 0
        for ques in task_obj.questions.all():
            matched = True
            curr_answer = Selected.objects.get(user=curr_user, question=ques, is_active=True)
            curr_choices = curr_answer.answer.all()
            for next_user in task_obj.user.all().exclude(id=curr_user.id):
                next_answer = Selected.objects.get(user=next_user, question=ques, is_active=True)
                next_choices = next_answer.answer.all()
                if set(curr_choices) != set(next_choices):
                    matched = False
                next_answer.is_active = False
                next_answer.save()
            if matched:
                score += 1
            curr_answer.is_active = False
            curr_answer.save()
            ques.consensus_reached = True
            ques.save()
        for user in task_obj.user.all():
            player, new = Player.objects.new_or_get(user)
            player.score += score
            player.save()
        task_obj.is_active = False
        task_obj.save()
