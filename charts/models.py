from django.db import models

# Create your models here.
Category=(
	("Technical","Technical"),
	("Personal","Personal"),
	("ZF","ZF"),
	("Visteon","Visteon"))
class SalesReport(models.Model):
	month=models.IntegerField()
	sales=models.FloatField(max_length=100)
	product=models.CharField(max_length=100)

class TechnicalSkills(models.Model):
	skills=models.CharField(max_length=100)
	scale=models.IntegerField()
	category=models.CharField(max_length=20,choices=Category,default="Technical")

	def __str__(self):
		return self.skills
