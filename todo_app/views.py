from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoforms
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model = Task
    template_name= 'task_detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):

    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbv')


def task_view(request):
    obj1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})

def task_delete(request,id):
    obj2=Task.objects.get(id=id)
    if request.method=='POST':
        obj2.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':obj2})
def task_update(request,id):
    obj=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'obj':obj,'form':form})