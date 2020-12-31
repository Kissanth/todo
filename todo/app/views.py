from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todo
# Create your views here.
y=todo.objects.all()
def view(request): 
	y=todo.objects.all()
	return render(request,'index.html',{'todo':y})
def addtodo(request):
	x = request.POST['content']
	new_item=todo(content=x)
	new_item.save()
	return HttpResponseRedirect('/todo/') 