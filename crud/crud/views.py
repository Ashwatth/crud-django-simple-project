from pyexpat.errors import messages
from django.shortcuts import render
from crud.models import company
from django.contrib  import messages
from crud.forms import cpnform 

def cpndisplay(request):
    results=company.objects.all()
    return render(request,'index.html',{"company":results})

def  cpninsert(request):
    if request.method=="POST":
        if request.POST.get("cpnname") and request.POST.get("cpnjob") and request.POST.get("cpnsalary"):
             savecpn=company()
             savecpn.cpnname=request.POST.get("cpnname")
             savecpn.cpnjob=request.POST.get("cpnjob")
             savecpn.cpnsalary=request.POST.get("cpnsalary")
             savecpn.save()
             messages.success(request,"The company" +savecpn.cpnname+" is saved successfully!!")
             return render(request,"create.html")
    else:
         return render(request,"create.html")
def cpnedit(request,id):
     getcpn=company.objects.get(id=id)
     return render(request,"edit.html",{"company":getcpn})
 
def cpnupdate(request,id):
    cpnupdate=company.objects.get(id=id)
    form=cpnform(request.POST,instance=cpnupdate)
    if form.is_valid():
         form.save()
         messages.success(request,"Company updated")
         return render(request,"edit.html",{"company":cpnupdate})

def cpndel(request,id):
    delcpn=company.objects.get(id=id)
    delcpn.delete()
    results=company.objects.all()
    return render(request,'index.html',{"company":results})
    
         