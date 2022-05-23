from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import StudentForm,BookForm,AdminForms,BookIssueForm
from .models import studentRecords,bookDataset,issueRecords

# Create your views here.

def home(request):
    return render(request,'home.html')

def Student(request):
    form=StudentForm
    if request.method=='POST':
        stud_form=StudentForm(request.POST)
        if stud_form.is_valid():
            stud_form.save()
            return redirect('/student')
    return render(request,'student.html',{'form':form})

def student_list(request):
    data=studentRecords.objects.all()
    return render(request,'studentlist.html',{'data':data})

def deletstudent(request,id):
    name=studentRecords.objects.get(id=id)
    name.delete()
    return redirect('/list')



def updatestudent(request,id):
    name=studentRecords.objects.get(id=id)
    form=StudentForm(instance=name)
    if request.method == 'POST':
        saveform=StudentForm(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatestudent.html',{'form':form})


def addstudent(request):
    form=StudentForm
    if request.method=='POST':
        saveform=StudentForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addstudent.html',{'form':form})


def Book(request):
    form=BookForm
    if request.method=='POST':
        bk_form=BookForm(request.POST)
        if bk_form.is_valid():
            bk_form.save()
            return redirect('/book')
    return render(request,'book.html',{'form':form})

def book_list(request):
    data=bookDataset.objects.all()
    return render(request,'booklist.html',{'data':data})

def deletebook(request,id):
    name=bookDataset.objects.get(id=id)
    name.delete()
    return redirect('/list')



def updatebook(request,id):
    name=bookDataset.objects.get(id=id)
    form=BookForm(instance=name)
    if request.method == 'POST':
        saveform=StudentForm(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatebook.html',{'form':form})


def addbook(request):
    form=BookForm
    if request.method=='POST':
        saveform=BookForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/lists')
    return render(request,'addbook.html',{'form':form})

def issueBook(request):
    form=BookIssueForm
    if request.method=='POST':
        bk_form=BookForm(request.POST)
        if bk_form.is_valid():
            bk_form.save()
            return redirect('/issuebook')
    return render(request,'book.html',{'form':form})

def issuebook_list(request):
    data=issueRecords.objects.all()
    return render(request,'issuebooklist.html',{'data':data})

def deleteissuebook(request,id):
    name=issueRecords.objects.get(id=id)
    name.delete()
    return redirect('/list')



def updateissuebook(request,id):
    name=issueRecords.objects.get(id=id)
    form=BookIssueForm(instance=name)
    if request.method == 'POST':
        saveform=StudentForm(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatebook.html',{'form':form})


def addissuebook(request):
    form=BookIssueForm
    if request.method=='POST':
        saveform=BookIssueForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/listss')
    return render(request,'addissuebook.html',{'form':form})





def register(request):
    form=AdminForms
    if request.method=='POST':
        admin_form= AdminForms(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('/register')
    else:
        form=AdminForms

    return render(request,'registration/adminregister.html',{'form':form})









