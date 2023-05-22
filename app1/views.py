from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    form= StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        form= StudentForm
    data = Student.objects.all()
    context ={
        'form': form,
        'data': data
    }
    return render(request, 'app1/index.html', context)


# Delete View
def delete_record(request, id):
    a =Student.objects.get(pk=id)
    a.delete()
    return redirect('/')


# Update View
def update(request,id):
    if request.method=='POST':
        data=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Student.objects.get(pk=id)
        form=StudentForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)