from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html',)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html', )
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html', )
    #return HttpResponse("this is services page")

def project(request):
    return render(request, 'project.html', )

def feature(request):
    return render(request, 'feature.html', )

def free_quote(request):
    return render(request, 'free_quote.html', )

def Our_Team(request):
    return render(request, 'Our_Team.html', )

def Testimonial(request):
    return render(request, 'Testimonial.html', )

def Page(request):
    return render(request, '404_Page.html', )

def contact(request):
    return render(request, 'contact.html', )
    #return HttpResponse("this is contact page")
def contact(request):
    return render(request, 'contact.html')
def getco(request):
    return render(render,'getco.html')
