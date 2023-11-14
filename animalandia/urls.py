"""animalandia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.api.router import router_user
from pet.api.router import router_pet, router_solicitudAdopcion, router_formularioVoluntario
from pet.api import views






schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('accounts.api.router')),
    path('api/', include(router_user.urls)),
    path('api/', include(router_pet.urls)),
    path('api/', include(router_solicitudAdopcion.urls)),
    path('api/', include(router_formularioVoluntario.urls)),

    #prueba

    path('aceptar-solicitud-adopcion/<int:solicitud_id>/', views.aceptar_solicitud_adopcion, name='aceptar_solicitud_adopcion'),
    path('denegar-solicitud-adopcion/<int:solicitud_id>/', views.denegar_solicitud_adopcion, name='denegar_solicitud_adopcion'),
    path('aceptar-solicitud-voluntario/<int:solicitud_id>/', views.aceptar_solicitud_voluntario, name='aceptar_solicitud_voluntario'),
    path('denegar-solicitud-voluntario/<int:solicitud_id>/', views.denegar_solicitud_voluntario, name='denegar_solicitud_voluntario'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# router_pet = DefaultRouter()
# router_solicitudAdopcion = DefaultRouter()
# router_formularioVoluntario = DefaultRouter()