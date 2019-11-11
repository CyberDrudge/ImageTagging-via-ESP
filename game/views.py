from django.shortcuts import render, redirect
from .utilities import check_submission
from questions.forms import ChoiceForm
from tasks.models import Task
from accounts.models import Player


# Create your views here.
def homepage(request):
    return render(request, 'game/base.html', {})


def thegame(request):
    if request.user.is_authenticated:
        task, new = Task.objects.new_or_get(request)
        template_name = 'tasks/task_view.html'
        context = {
            'task': task,
        }
        return render(request, template_name, context)

    return redirect('/login/')


def action(request):
    a = request.POST.getlist('answers')
    curr_task_id = request.POST.get('task')
    curr_task = Task.objects.get(id=curr_task_id)
    for ques in curr_task.questions.all():
        choices_all = ques.secondary_image.all()
        selected = [x.id for x in choices_all if str(x.id) in a]
        if selected:
            form_data = {
                'question': ques.id,
                'answer': selected
            }
            form = ChoiceForm(form_data)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.question = form.cleaned_data['question']
                instance.save()
                instance.answer.set(form.cleaned_data['answer'])
                instance.save()
            else:
                print("Form Invalid")
                break
        else:
            raise Exception("Please Select a viable option.")
    player, new = Player.objects.new_or_get(request.user)
    player.current_task = None
    player.save()
    check_submission(request, curr_task)
    return render(request, 'tasks/task_completed.html', {})
