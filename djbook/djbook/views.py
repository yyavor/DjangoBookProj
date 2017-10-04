from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime, timedelta


def hello(request):
    return HttpResponse("Helloooooo")


def current_date(request):
    now = datetime.now()
    date_template = get_template('current_date.html')
    html_date_text = date_template.render({'date': now})
    return HttpResponse(html_date_text)


def current_date_with_offset(request, hours_offset):
    try:
        hours_offset = int(hours_offset)
    except ValueError:
        raise Http404
    date = datetime.now() + timedelta(hours=hours_offset)
    return render(request, 'future_date.html', {'current_date': datetime.now(),
                                                'future_date': date})
