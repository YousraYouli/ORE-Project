from django.urls import path
from . import views

urlpatterns = [

        path("index", views.index, name="index"),
   		path("",views.home,name="home"),
        path("about",views.about,name="about"),
        path("contact",views.contact,name="contact"),
        path("error",views.error,name="error"),
        path("layout",views.layout,name="layout"),
        path("course",views.course,name="course"),
        path("install",views.instal,name="instal"),
        path("docs",views.doc,name="doc"),

  
]	

