from django.urls import path
from . import views

urlpatterns = [

		path("register",views.register,name="register"),
		path("login",views.loginPage,name="login"),
		path("logout",views.logoutPage,name="logout"),
        path("index", views.index, name="index"),
   		path("wiki/<str:title>",views.entry,name="wiki-entry"),
  		path("search",views.search,name="search"),
    	path("search_results/<str:query>/<str:results>",views.search_results,name="search_results"),
   		path("",views.home,name="home"),
        path("about",views.about,name="about"),
        path("contact",views.contact,name="contact"),
        path("wiki/<str:title>",views.entry,name="wiki-entry"),
        path("error",views.error,name="error"),
        path("layout",views.layout,name="layout"),
        path("course",views.course,name="course"),
        path("instal",views.instal,name="instal"),
        path("doc",views.doc,name="doc"),
        path("origine",views.origine,name="origine"),
      # path("mai",views.mai,name="mai"),
    #   path("success",views.success,name="success"),
		
  
]	

