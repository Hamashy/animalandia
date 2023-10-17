from rest_framework.routers import DefaultRouter

from pet.api.views import FormularioAdopcionApiViewSet, PetApiViewSet, SolicitudAdopcionApiViewSet






router_pet = DefaultRouter()
router_solicitudAdopcion = DefaultRouter()
router_formularioVoluntario = DefaultRouter()

router_pet.register(prefix='pets', basename='pets', viewset=PetApiViewSet)
router_solicitudAdopcion.register(prefix='solicitudAdopcion', basename='solicitudAdopcion', viewset=SolicitudAdopcionApiViewSet)
router_formularioVoluntario.register(prefix='formularioVoluntario', basename='formularioVoluntario', viewset=FormularioAdopcionApiViewSet)


