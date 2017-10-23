# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Comment
from django.db.models import Count

# Create your views here.
def index(request):
    if not 'id' in request.session:
        return redirect('/')
    context={
        'user': User.objects.get(id=request.session['id']),
        'other_user': User.objects.exclude(id=request.session['id']),
        # 'other_users': Comment.objects.exclude(user__id=request.session['id']).annotate(comCount=Count('comment')).order_by('comCount'),
    }
    return render(request,'comment_app/index.html', context)

def add(request, id):
    context={
        'user': User.objects.get(id=id),
        'comments': Comment.objects.filter(user__id=request.session['id']),
    }
    return render(request,'comment_app/user.html',context)

def create(request):
    user = User.objects.get(id=request.session['id'])
    Comment.objects.create(comment=request.POST['comment'], user=user)
    return redirect('/comment')
