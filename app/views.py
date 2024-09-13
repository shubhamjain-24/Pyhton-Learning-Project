from django.shortcuts import render, redirect
from .models import student

# Create your views here.
def index(request):
    data = student.objects.all()  # Fetch all student records
    context = {"data": data}
    return render(request, 'index.html', context)


def updateData(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        edit = student.objects.get(id=id) 
        edit.name =name
        edit.email =email
        edit.age= age
        edit.gender = gender
        edit.save()
        
        return redirect("/")
    d = student.objects.get(id=id)  
    context = {"d": d}
    return render(request, 'update.html', context)

def deleteData(request,id):
    d = student.objects.get(id=id)  
    d.delete()
    return redirect('/')

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        # Insert the new student record
        query = student(name=name, email=email, age=age, gender=gender)
        query.save()

        # Redirect to avoid form re-submission on refresh
        return redirect('index')

    # Fetch all student records to display on GET request
    data = student.objects.all()
    context = {"data": data}
    

    
    return render(request, 'index.html', context)
