from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from pet.api.serializers import FormularioVoluntarioSerializer, PetSerializer, SolicitudAdopcionSerializer
from pet.models import FormularioVoluntario, Pet, SolicitudAdopcion


class PetApiViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminUser]

class SolicitudAdopcionApiViewSet(ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer
    permission_classes = [IsAdminUser]

class FormularioAdopcionApiViewSet(ModelViewSet):
    queryset = FormularioVoluntario.objects.all()
    serializer_class = FormularioVoluntarioSerializer
    permission_classes = [IsAdminUser]


# Vista para aceptar la solicitud de adopción
@csrf_exempt
def aceptar_solicitud_adopcion(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=solicitud_id)
    
    # Cambiar el estado de la solicitud de adopción
    solicitud.estado = 'aceptado'  # Cambiar el estado a 'aceptado' o utilizar modelos.TextChoices
    solicitud.save()

    # Cambiar el estado de la mascota a 'Adoptado'
    mascota = solicitud.id_mascota
    mascota.estado = 'Adoptado'  # Cambiar el estado de la mascota
    mascota.save()

    return JsonResponse({'message': 'Solicitud de adopción aprobada correctamente.'})

# Vista para denegar la solicitud de adopción

@csrf_exempt
def denegar_solicitud_adopcion(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=solicitud_id)
    
    # Cambiar el estado de la solicitud de adopción
    solicitud.estado = 'denegado'  # Cambiar el estado a 'denegado' o utilizar modelos.TextChoices
    solicitud.save()

    # Cambiar el estado de la mascota a 'Disponible'
    mascota = solicitud.id_mascota
    mascota.estado = 'Disponible'  # Cambiar el estado de la mascota
    mascota.save()

    return JsonResponse({'message': 'Solicitud de adopción denegada correctamente.'})


# Vista para aceptar la solicitud de voluntariado
@csrf_exempt
def aceptar_solicitud_voluntario(request, solicitud_id):
    solicitud = get_object_or_404(FormularioVoluntario, pk=solicitud_id)
    
    # Cambiar el estado de la solicitud de voluntario
    solicitud.estado = 'aceptado'  # Cambiar el estado a 'aceptado' o utilizar modelos.TextChoices
    solicitud.save()

    return JsonResponse({'message': 'Solicitud de voluntario aceptada correctamente.'})

# Vista para denegar la solicitud de voluntariado
@csrf_exempt
def denegar_solicitud_voluntario(request, solicitud_id):
    solicitud = get_object_or_404(FormularioVoluntario, pk=solicitud_id)
    
    solicitud.estado = 'denegado'  # Cambiar el estado a 'denegado' o utilizar modelos.TextChoices
    solicitud.save()

    return JsonResponse({'message': 'Solicitud de voluntario denegada correctamente.'})






# class ConsultorioApiViewSet(ModelViewSet):
#     queryset = Consultorio.objects.all()
#     serializer_class = ConsultorioSerializer
#     permission_classes = [IsAdminUser]