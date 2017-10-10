from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from datetime import datetime, timedelta
from djbook.forms import ContactForm
from django.core.mail import send_mail, get_connection


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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': "Put your subject here"})

    return render(request, 'contact_form.html', {'form': form})
