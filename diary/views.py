from django.shortcuts import render, redirect
from .models import Diary
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    username    = request.user
    diary       = username.diary_set.all().order_by('-id')
    template    = 'diary/index.html'
    context     = { 'diary' : diary }
    return render(request,template,context)

def add(request):

    if (request.method == "POST"):
        title   =  request.POST['title']
        content =  request.POST['content']
        user    =      request.user
        Diary.objects.create(diary_title=title,diary_content=content,user=user)

        return redirect('index')

    template    = 'diary/add.html'
    context     =  {}
    return render(request,template,context)