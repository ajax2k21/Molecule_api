from rest_framework import serializers
from .models import Molecule

class MoleculeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ['id', 'LSN', 'sdf']