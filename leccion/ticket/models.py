# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ticket(models.Model):
	
    fechaEmision=models.DateField()
    Precio=models.FloatField()
    Adquiriente=models.CharField(max_length=12)
    Puesto=models.IntegerField()
    
    YEAR_IN_SCHOOL_CHOICES = (
        ('ciudad 1', 'Guayaquil'),
        ('ciudad 2', 'Quito'),
        ('ciudad 3', 'Manta'),
        ('ciudad 4', 'Machala'),
        ('ciudad 5', 'Babahoyo'),
    )
    Origen = models.CharField(
        max_length=20,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )
    Destino = models.CharField(
        max_length=20,
        choices=YEAR_IN_SCHOOL_CHOICES,
    )