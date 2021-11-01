from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def userlogin(request):
    return HttpResponse("User Login Page")


def usersignup(request):
    return HttpResponse("User Signup Page")


def quotations(request):
    return HttpResponse("Quotations")


def invoices(request):
    return HttpResponse("invoices")


def purchases(request):
    return HttpResponse("purchases")


def productservices(request):
    return HttpResponse("productservices")
