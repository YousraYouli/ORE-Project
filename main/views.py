from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .forms import CreateUserForm
from django.urls import reverse
from . import util
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import json
import os
from django.views.decorators.csrf import csrf_exempt

    
def home(request):
    form = CreateUserForm()
    
    if request.method == "POST" :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context={'form':form}
    return render(request, 'main/home.html', context) 
def origine(request):
    return render(request, 'main/origine.html')
def doc(request):
    return render(request, 'main/doc.html')
def about(request):
    return render(request, 'main/about.html')
def contact(request):
    return render(request, 'main/contact.html')
def course(request):
    return render(request, 'main/course.html')
def instal(request):
    return render(request, 'main/instal.html')
def error(request):
    return render(request, 'main/error.html')
def layout(request):
    return render(request, 'main/layout.html')
def search(request):
    return render(request, 'main/search.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST" :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    #     return redirect('login')
    context={'form':form}
    return render(request, 'main/register.html', context) 
   
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passw = request.POST.get('password')
        user = authenticate(request, username=username, password=passw)
        if user:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        messages.error(request,'Login Error')  
    return render(request,'main/home.html')

def logoutPage(request):
    logout(request)
    return redirect('home')

def entry(request, title ) :
    if title not in util.list_entries() :
        return render(request,"main/error.html", {
            "error_title": "Error 404",
            "error": "The course That you requested does not exist !"})
    return render(request, "main/entry.html", {'title': title, 'content': util.convert_markdown_to_html(util.get_entry(title))})

#markdown exampels

def index(request):
    return render(request, "main/index.html", {
        "entries": util.list_entries()
    })



def search(request):
    if request.method == "POST":
        query = request.POST.get('q')
        if query == "" or query == None:
            return render(request, "main/error.html", {"error_title": "Error 400", "error": f"You submitted an empty query!"})
        lst = util.list_entries()
        entries = [entry.lower() for entry in lst]
        if query.lower() in entries:
            return HttpResponseRedirect(reverse("main:wiki-entry", args=(lst[entries.index(query.lower())],)))
        else:
            results = []
            for entry in util.list_entries():
                if query.lower() in entry.lower():
                    results.append(entry)
            if results == []:
                results = ' '
            else:
                results = ','.join(results)
            return HttpResponseRedirect(reverse("main:search_results", args=(query,results))) 
            #render(request, "encyclopedia/search.html", {'results': results,'q': request.POST.get('q')})
    else:
        return render(request, "encyclopedia/error.html", {"error_title": "Error 403", "error": f"The request method {request.method} is not allowed !"})

def search_results (request,query,results):
    if results == None or query == None:
        return render(request, "main/error.html", {"error_title": "Error 405", "error": f"You are not allowed to access this page directly !"})
    if results == ' ':
        return render(request,"main/search.html", {'results': [],'q': query})  
    return render(request, "main/search.html", {'results': results.split(','),'q': query})


#""" def indexx(request):
  #  form=ContactForm(request.POST or None)
  # "" if request.method=='POST':
    #    form=ContactForm()
    #if form.is_valid():
 #       print('the form was valid')
 #""   else:
  #      form=ContactForm()
   # return render(request,"main/indexx.html",{
    #""   'form=':form
   # }) """

def indexx(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
           # phone=form.cleaned_data['phone']
            send_mail(name, message, email, ["yousra17012004@gmali.com"])
           # try:
            #    send_mail(subject, message, from_email, ["admin@example.com"])
            #except BadHeaderError:
             #   return HttpResponse("Invalid header found.")
            #return redirect("success")
    return render(request, "main/indexx.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")

# to login via facebook
def Logil(request):
    return render(request, 'main/Logil.html')

@csrf_exempt
def execute(request):
    if request.method == "POST":
        code = json.loads(request.body.decode())['code']
        with open("/tmp/ore_exec", "w") as f:
            f.write(code)

        output = os.popen("orepl -a /tmp/ore_exec").read()
        return JsonResponse({"output": output})
