from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from pet.models import FormularioVoluntario, Pet, SolicitudAdopcion




class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class SolicitudAdopcionSerializer(ModelSerializer):
    class Meta:
        model = SolicitudAdopcion
        fields = '__all__'

class FormularioVoluntarioSerializer(ModelSerializer):
    class Meta:
        model = FormularioVoluntario
        fields = '__all__'