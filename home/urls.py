from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("project",views.project, name='project'),
    path("feature",views.feature, name='feature'),
    path("free_quote",views.free_quote, name='free_quote'),
    path("Our_Team",views.Our_Team, name='Our_Team'),
    path("Testimonial",views.Testimonial, name='Testimonial'),
    path("Page",views.Page, name='Page'),
]
