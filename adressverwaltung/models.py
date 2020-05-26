from django.db import models

# Create your models here.
class Person(models.Model): #() gibt an, dass Modell ein Django-Modell ist -> Django weiß, dass es in DB gespeichert werden soll
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    housenumber  = models.IntegerField()
    city = models.CharField(max_length = 100)
    zipCode = models.IntegerField() #keine max_length bei Int-Feldern -> führt zu Warnings bei migration
    phone = models.CharField(max_length = 100)
    mail = models.CharField(max_length = 100)    
    #Modell erstellen, dass alle Datenfelder enthält, die auf der Website angezeigt werden sollen
    
    def publish(self): #Methode für Veröffentlichung
        self.save()

    def __str__(self): #Nachname wird zurückgegeben
        return self.lastName
