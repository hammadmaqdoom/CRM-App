from os import access
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Company(models.Model):
    companyID = models.IntegerField(primary_key=True)
    companyName =models.CharField(max_length=64)
    companyEmail = models.EmailField( max_length=254)
    companyPhoneNumber = models.PhoneNumberField()
    is_client = models.BooleanField(default=True)

class Users(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.CharField(max_length=1000)
    password = models.CharField(max_length=64)
    ACCESS_LEVEL = (
        ('0', 'Admin'),
        ('1', 'Business'),
        ('2', 'CompanyUser'),
    )
    accessLevel = models.CharField(max_length=1, choices=ACCESS_LEVEL)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)

class Business(models.Model):
    businessID = models.IntegerField(primary_key=True)
    businessName = models.CharField(max_length=64)
    ORGANISATION_TYPE = (
        ('SP', 'SoleProprietor'),
        ('P', 'Partnership'),
        ('PL', 'PrivateLimited'),
        ('PBL', 'PublicLimited')
    )
    organisationType = models.CharField(max_length=3, choices=ORGANISATION_TYPE)
    businessType = models.CharField(max_length=64)
    currency = models.IntegerField()

class CompanyUsers(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    USER_TYPE = (
        ('S', 'Sales'),
        ('P', 'Purchases')
    )
    userType = models.CharField(max_length=1, choices=USER_TYPE)

class ProductsAndServices(models.Model):
    itemID = models.IntegerField(primary_key=True)
    isProduct = models.BooleanField(primary_key=True)
    itemDescription = models.CharField(max_length=500)
    rate = models.IntegerField()

class Sales(models.Model):
    salesID = models.IntegerField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    itemID = models.ForeignKey(ProductsAndServices, on_delete=models.CASCADE)
    STAT = (
        ('A', 'Approved'),
        ('NA', 'NotApproved')
    )
    status = models.CharField(max_length=2, choices=STAT)

class Purchases(models.Model):
    billID = models.IntegerField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.CASCADE)
    businessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    itemID = models.ForeignKey(ProductsAndServices, on_delete=models.CASCADE)
    STAT = (
        ('A', 'Approved'),
        ('NA', 'NotApproved')
    )
    status = models.CharField(max_length=2, choices=STAT)

class Transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    billID = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    salesID = models.ForeignKey(Sales, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    debit = models.IntegerField()
    credit = models.IntegerField()