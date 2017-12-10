from django.db import models

# Create your models here.

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
    cnpe = models.ForeignKey(CNPE, on_delete=models.CASCADE)
    reseaux = models.ManyToManyField(Reseau)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    def __str__(self):
        return self.nom + ' ' + self.prenom
