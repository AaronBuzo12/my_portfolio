from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ContactMessageForm

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


def project_detail(request, id):

	project = Project.objects.get(id=id)
	return render(request, "main/project_detail.html", {"project": project})




def contact(request):
	form = ContactMessageForm()

	if request.method == "POST":

		form = ContactMessageForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request, "Your message has been sent successfully!")
			return redirect("contact")


	return render(request, "main/contact.html", {"form":form}
	)





