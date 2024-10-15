from django.db import models


# Logo Model: ENG4033, ENG1118, ENG4021
class Logo(models.Model):
    image = models.ImageField(upload_to='logos/')  # Store all logos in this location
    type = models.CharField(max_length=100, 
        choices={  # Database name : Custom name for user
        'microcontroladores': 'ENG4033 – Projeto de Microcontroladores', 
        'matlab': 'ENG1118 – Matlab', 
        'software': 'ENG4021 - Projeto Integrado de Software',
        } ) 
    color = models.CharField(max_length=100)  # Store color of logo

    def __str__(self):
        return self.type


# Class Model: ENG4033, ENG1118, ENG4021
class Class(models.Model): 
    name = models.CharField(max_length=100) 
    type = models.CharField(max_length=100, 
        choices={  # Database name : Custom name for user
        'microcontroladores': 'ENG4033 – Projeto de Microcontroladores', 
        'matlab': 'ENG1118 – Matlab', 
        'software': 'ENG4021 - Projeto Integrado de Software',
        } ) 
    
    active = models.BooleanField(default=True)
    logo = models.ForeignKey(Logo, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True) 
    

    def __str__(self):
        return "%s: %s" % (self.type, self.name)
    
    class Meta: 
        verbose_name = "class" 
        verbose_name_plural = "classes" 

