
from django.shortcuts import get_object_or_404,redirect, render
from .models import Student
from. forms import StudentForm


# Create your views here.
def addview(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form=StudentForm()
    else:
        form=StudentForm()
    stu=Student.objects.all()
    return render(request,'enroll/addview.html',{'form':StudentForm(),'stu':stu})


def updateview(request,id):
    obj = get_object_or_404(Student, id = id)
    if request.method=="GET":
        form=StudentForm(instance=obj)
        return render(request,'enroll/updateview.html',{'form':form})
    else:
        form =StudentForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
            return redirect('/')
   
def deleteview(request,id):
    
    if request.method=="POST":
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect('/'+id)



# def deleteview(request, id):
#     obj=get_object_or_404(Student,pk=id)
#     if request.method=="POST":
#         obj.delete()
#         return redirect('/')

