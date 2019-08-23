from django.shortcuts import render, render_to_response
from django.views.generic import UpdateView
from datetime import date

from .models import dataform

# Create your views here.

def submitdetails(request):
	fname = request.POST.get("firstname")
	lname = request.POST.get("lastname")
	dataform(firstname=fname, lastname=lname).save()
	return render(request, "form.html", {"msg": "Data added successfully"})