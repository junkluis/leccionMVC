from rest_framework import serializers
from .models import *

class ticketSerializer(serializers.ModelSerializer):

    class Meta:
        model = ticket
        fields = ('fechaEmision', 'Precio', 'Adquiriente', 'Puesto', 'Origen', 'Destino')