from django.shortcuts import render
from django.http import HttpResponse
from .models import Paste, Comment
from django.template import loader

#Create your views here.

def index(request):
    if request.method =="GET":
        return HttpResponse("Hey, I work")

def retrieve_objects(request, paste_url):
    if request.method=="GET":
        paste_list = Paste.objects.all()
        template = loader.get_template('templates.html')
        context = {
                'Paste_list' : paste_list,
                }
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        print(1)
        obj = Paste.objects.create(name = request.POST.get('name'),
                                    uploader = request.POST.get('uploader'),
                                    url = request.POST.get('url'),
                                    content = request.POST.get('content')
                                    )
        paste_list = Paste.objects.all()
        template = loader.get_template('templates.html')
        context = {
                'Paste_list' : paste_list,
                }
        return HttpResponse(template.render(context, request))

