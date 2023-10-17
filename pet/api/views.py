from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from pet.api.serializers import FormularioVoluntarioSerializer, PetSerializer, SolicitudAdopcionSerializer
from pet.models import Pet, SolicitudAdopcion


class PetApiViewSet(ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminUser]

class SolicitudAdopcionApiViewSet(ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = SolicitudAdopcionSerializer
    permission_classes = [IsAdminUser]

class FormularioAdopcionApiViewSet(ModelViewSet):
    queryset = SolicitudAdopcion.objects.all()
    serializer_class = FormularioVoluntarioSerializer
    permission_classes = [IsAdminUser]







# class ConsultorioApiViewSet(ModelViewSet):
#     queryset = Consultorio.objects.all()
#     serializer_class = ConsultorioSerializer
#     permission_classes = [IsAdminUser]