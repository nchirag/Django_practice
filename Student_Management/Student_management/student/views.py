from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    return render(request,'index.html')

def student_list(request):
    students = Student.objects.all()
    return render(request,'student_list.html',context = {'students':students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        department = request.POST.get('department')
        status = request.POST.get('status') =='on'

        student = Student.objects.create(name=name,age=age,contact=contact,department=department,status=status)
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'action': 'Add'})
    
def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

def edit_student(request,id):
    student = Student.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        department = request.POST.get('department')
        status = request.POST.get('status') =='on'
        student = Student.objects.create(name=name,age=age,contact=contact,department=department,status=status)
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'action': 'Edit','student':student})