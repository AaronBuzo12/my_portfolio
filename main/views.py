from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
	projects = Project.objects.all()

	return render(request, "main/index.html", {
	"projects": projects
	})


def about(request):
	return render(request, "main/about.html")



def projects(request):
	projects = Project.objects.all()
	return render(request, "main/projects.html", {"projects": projects})


def contact(request):
	return render(request, "main/contact.html")


