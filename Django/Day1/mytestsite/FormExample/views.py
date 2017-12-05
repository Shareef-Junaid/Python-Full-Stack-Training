from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        # getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # adding the values in a context variable
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        # getting our showdata template
        template = loader.get_template('showdata.html')

        # returning the template
        return HttpResponse(template.render(context, request))
        # return HttpResponse("Method POST")
    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
        # return HttpResponse("Not POST")


@csrf_exempt
def add_numbers(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1+num2
        return HttpResponse('Addition is %s' % result)
    else:
        template = loader.get_template('addition.html')
        return HttpResponse(template.render())

