from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Member(models.Model):
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	email = models.EmailField()
	dateNaissance = models.DateTimeField(auto_now=False, auto_now_add=False)
	sexe = models.CharField(max_length=10, choices=[('homme', 'homme'), ('femme', 'femme')])
	profession = models.CharField(max_length=50)
	numTel = models.IntegerField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return "%s %s" %(self.nom, self.prenom)
