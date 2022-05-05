from re import X
from django.shortcuts import render
from .models import TodoList
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

#Hello programmers, this is nothing but some tests to make sure that Git is Working


def index(request):
    todo_list = TodoList.objects.order_by('-pub_date')[:5]
    context = {'todo_list':todo_list}
    return render(request, 'my_todo_app/index.html', context)

#Add Items In The Database
def add(request):
    x = request.POST['todo']
    time = timezone.now()
    if x != '':
        TodoList.objects.create(my_todo=x, pub_date=time)
    return HttpResponseRedirect(reverse('salah:index'))


#Delete Items In The Database
def delete(request, todo_id):
    item = TodoList.objects.get(pk=todo_id)
    item.delete()
    return HttpResponseRedirect(reverse('salah:index'))
