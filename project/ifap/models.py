from django.db import models

# Create your models here.

class Classe(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def getName(self):
        return self.name

class Ordre(models.Model):
    ordre = models.CharField(max_length=100,unique=True)

    def getOrdre(self):
        return self.ordre 

class Famille(models.Model):
    famille = models.CharField(max_length=100,unique=True)

    def getFamille(self):
        return self.famille

class Animal(models.Model):
    ncom    = models.CharField(max_length=50,unique=True)
    nsci    = models.CharField(max_length=50,unique=True)
    classe  = models.ForeignKey(Classe,on_delete=models.CASCADE)
    ordre   = models.ForeignKey(Ordre,on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille,on_delete=models.CASCADE)

    def getNcom(self):
        return self.ncom


