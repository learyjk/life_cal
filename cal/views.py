from django.shortcuts import render, get_object_or_404, redirect
from week.models import Week, Note
from week.forms import NoteForm


def index(request):
    if request.user.is_authenticated:

        week_list = Week.objects.filter(user_id=request.user.id).order_by('week_number')

        context = {
            'week_list': week_list,
            'cal_width': range(52),
        }
        return render(request, 'cal/index.html', context)

    else:
        return redirect('login')


def week_view(request, week_number):
    if request.method == "POST":
        week = get_object_or_404(Week, week_number=week_number, user_id=request.user.id)
        form = NoteForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            new_note = Note(text=form['text'], week=week)
            new_note.save()

        context = {
            'week': week,
            'form': NoteForm(),
            'notes': week.note_set.all(),
        }
        return render(request, 'cal/week_view.html', context)
    else:
        week = get_object_or_404(Week, week_number=week_number, user_id=request.user.id)

        context = {
            'week': week,
            'form': NoteForm(),
            'notes': week.note_set.all(),
        }
        return render(request, 'cal/week_view.html', context)


def remove_note(request, note_id):
    note = Note.objects.get(id=note_id)
    week = Week.objects.get(id=note.week.id, user_id=request.user.id)
    note.delete()
    return redirect('week_view', week_number=week.week_number)
