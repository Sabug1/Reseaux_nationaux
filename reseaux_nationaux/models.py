from django.db import models
from django.contrib.auth.models import User

class CNPE(models.Model):
    nom = models.CharField(max_length=200)
    palier = models.CharField(max_length=200, choices=(
              ('CPY','CPY'),('CP0','CP0'),('P4','P4'),("P'4","P'4"),('H4','H4'),('N4','N4')
              ))
    def __str__(self):
        return self.nom + ' (' + self.palier + ')'

class Reseau(models.Model):
    nom = models.CharField(max_length=200, choices=(
              ('ROB','Robinetterie'),('RCP','Recipients'),('TUY','Tuyauteries'),("AUTO","Automatisme"),('ELEC','Elec'),('MTOUR','Machines tournantes')
              ))
    def __str__(self):
        return self.nom


class Metier(models.Model):
    nom = models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Personne(models.Model):
    #vient de django et gère les mdp
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #vient de nous
    cnpe = models.ForeignKey(CNPE, on_delete=models.SET_NULL, null=True)
    reseaux = models.ManyToManyField(Reseau)
    telephone = models.CharField(max_length=200)
    metier = models.ForeignKey(Metier, on_delete=models.PROTECT)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
