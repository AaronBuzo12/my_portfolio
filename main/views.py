from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
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
	search = request.GET.get("search", "")


	projects = Project.objects.all()

	if search:
		projects = projects.filter(
			title__icontains=search) | projects.filter(
			description__icontains=search
			)

	return render(request, "main/projects.html", { "projects": projects, "search": search,})	



def project_detail(request, id):

	project = Project.objects.get(id=id)
	return render(request, "main/project_detail.html", {"project": project})




def contact(request):
	form = ContactMessageForm()

	if request.method == "POST":

		form = ContactMessageForm(request.POST)

		if form.is_valid():
			contact_message = form.save()

			send_mail(subject=f"New message from {contact_message.name}",

			message=contact_message.message,

			from_email=contact_message.email,

			recipient_list=["aaronbuzo15@gmail.com"],
			)

			messages.success(request, "Your message has been sent successfully!")
			return redirect("contact")


	return render(request, "main/contact.html", {"form":form}
	)





