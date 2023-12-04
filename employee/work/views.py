from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm
from work.models import Emp
from work.forms import bookForm
from work.models import book
from work.models import Movies,Mobile
from work.models import Students
from work.forms import MovieForm
from work.forms import PersonForm
from work.forms import MobileForm
from work.forms import StudentForm



# Create your views here.
class Employee(View):
 def get(self,request):
    form=EmpForm()
    return render(request,"add.html",{"form":form})
 #create post
 def post(self,request):
   form=EmpForm(request.POST)
   
   if form.is_valid():
     print(form.cleaned_data)
     Emp.objects.create(**form.cleaned_data)
     
     return render(request,"add.html",{"form":form})
   else:
     return render(request,"add.html",{"form":form})
     

class bookview(View):
  def get(Self,request):
    form=bookForm()
    return render(request,"book.html",{"form":form})  

  def post(self,request): 
    form=bookForm(request.POST)

    if form.is_valid():
      form.save()
      # print(form.cleaned_data)
      # book.objects.create(**form.cleaned_data)
      print("created")
      return render(request,"book.html",{"form":form})
    else:
      return render(request,"book.html",{"form":form})
                          

class  moviesview(View):
  def get (self,request):
    form=MovieForm()
    return render(request,"movie.html",{"form":form})
  
  def post(self,request):
    form=MovieForm(request.POST)

    if form.is_valid():
      print(form.cleaned_data)
      Movies.objects.create(**form.cleaned_data) 
      return render(request,"movie.html",{"form":form})
    else:
      return render (request,"movie.html",{"form":form}) 
    

class Studentview(View):
  def get(self,request):
    form=StudentForm()
    return render(request,"student.html",{"form":form})
  
  def post(self,request):
    form=StudentForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      Students.objects.create(**form.cleaned_data)
      return render(request,"student.html",{"form":form})
    else:
      return render(request,"student.html",{"form":form})
    
class studentDetailView(View):
  def get(self,request,**kwargs):
    print(kwargs)
    id = kwargs.get('pk')
    qs=Students.objects.get(id=id)
    return render(request,"students.html",{"data":qs})  
     


class Booklist(View):
  def get(self,request):
    qs=book.objects.all()
    return render(request,"booklist.html",{"qs":qs})

class Book_detailView(View):
  def get(self,request,*args,**kwargs):
    id=5
    qs=book.objects.get(id=id)
    return render(request,'book_details.html',{"data":qs})

  
class Personview(View):
  def get(self,request):
    form=PersonForm()
    return render(request,"person.html",{"form":form})
  
  def post(self,request):
    form=PersonForm(request.POST)

    if form.is_valid():
      form.save()
      print("created")

      return render(request,"person.html",{"form":form})
    else:
      return render(request,"person.html",{"form":form})
    
class Mobileview(View):
  def get(self,request):
    form=MobileForm()
    return render(request,"mobile.html",{"form":form})

  def post(self,request):
    form=MobileForm(request.POST)
    if form.is_valid():
      form.save()
      print("created")
      form = MobileForm()
      return render(request,"mobile.html",{"form":form})
    else:
      return render(request,"mobile.html",{"form":form})
    
class MobileList(View):
    def get(self,request):
      all = Mobile.objects.all()
      return render(request, "mobilelist.html",{"all":all})   
    


class Book_delete(View):
  def get(self,request,*args,**kwargs):
    id=kwargs.get("pk") 
    book.objects.get(id=id).delete()
    return redirect('book-al')   
    


    



