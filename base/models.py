from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Taskai(models.Model):
    '''
    "One to many relationship" (one user can have multiple items under his name)
    upon user deletion - delete everything related to the user. CASCADE - to delete SET_NULL - to keep.
    Null - it CAN be an empty field in the database
    Blank - allowing to submit a blank form value
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    diena = models.DateField(auto_now_add=False)
    pristatymai = models.IntegerField()
    pristatymai_pakuotes = models.IntegerField()
    uzsakymai = models.IntegerField()
    uzsakymai_pakuotes = models.IntegerField()
    km = models.IntegerField()
    arbata = models.IntegerField()
    apie = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.diena)  # very important to add str when displaying by date... https://www.youtube.com/watch?v=xKi87JuIWRM this error and this fix

    class Meta:
        ordering = ['diena']

