from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
# Create your views here.

User = get_user_model()

from .forms import UserForm
from .models import Member


class SubsView(View):
	def get(self, request):
		form = UserForm()
		return render(request, "subs.html", {"form": form})

	def post(self, request):
		form = UserForm( request.POST or None )
		if form.is_valid():
			username = form.cleaned_data["username"]
			nom = form.cleaned_data["nom"]
			prenom = form.cleaned_data["prenom"]
			email = form.cleaned_data["email"]
			date = form.cleaned_data["dateNaissance"]
			password = form.cleaned_data["dateNaissance"]
			sexe = form.cleaned_data["sexe"]
			profession = form.cleaned_data["profession"]
			num = form.cleaned_data["numTel"]

			user = User(username=username)
			user.set_password(password)
			user.save()

			new_member = Member(nom=nom, prenom=prenom, email=email, dateNaissance=date, sexe=sexe, profession=profession, numTel=num)
			new_member.save()

			member = authenticate(username=user.username, password=password)
			login(request, member)

			context = {
				"nom": nom,
				"prenom": prenom,
				"date": date,
			}

			return render(request, "welcome.html", context)

		return render(request, "fail.html", {})