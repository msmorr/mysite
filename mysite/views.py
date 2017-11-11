from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail, get_connection

def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render({'current_date' : now})
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date' : now}) #render consolidates the above commented steps

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
    return render(request, 'hours_ahead.html', {'offset' : offset, 'datetime' : dt})

def display_meta(request):
    """displays metadata about the user (IP address, browser, etc.)"""
    values = request.META
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)   # Check to see if request has been submitted; otherwise display blank contact form
        if form.is_valid(): # check to see if form contains valid data
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend') # used in development - doesn't require an email server
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )

    return render(request, 'contact_form.html', {'form': form}) # if form doesn't have valid data, reloads the contact form

def thanks(request):
    return render(request, 'thanks.html')