from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from week.models import Week


def index(request):

    week_list = Week.objects.filter(user_id=request.user.id).order_by('week_number')

    context = {
        'week_list': week_list,
        'cal_width': range(52),
    }
    return render(request, 'cal/index.html', context)


def week_view(request, week_number):
    week = get_object_or_404(Week, week_number=week_number, user_id=request.user.id)

    context = {
        'week': week
    }

    return render(request, 'cal/week_view.html', context)

    response = "You're looking at week number %s."
    return HttpResponse(response % week_number)
