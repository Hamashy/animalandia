from django.contrib import admin

from pet.models import FormularioVoluntario, Pet, SolicitudAdopcion

# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass




@admin.register(FormularioVoluntario)
class FormularioVoluntarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_usuario', 'estado']
    actions = ['aceptar_solicitudes', 'denegar_solicitudes']

    def aceptar_solicitudes(self, request, queryset):
        for formulario in queryset:
            formulario.aceptar_solicitud()

    def denegar_solicitudes(self, request, queryset):
        for formulario in queryset:
            formulario.denegar_solicitud()

    aceptar_solicitudes.short_description = "Aceptar solicitudes seleccionadas"
    denegar_solicitudes.short_description = "Denegar solicitudes seleccionadas"



@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_usuario', 'id_mascota', 'estado']
    actions = ['aceptar_solicitudes', 'denegar_solicitudes']

    def aceptar_solicitudes(self, request, queryset):
        for solicitud in queryset:
            solicitud.aceptar_solicitud()

    def denegar_solicitudes(self, request, queryset):
        for solicitud in queryset:
            solicitud.denegar_solicitud()

    aceptar_solicitudes.short_description = "Aceptar solicitudes seleccionadas"
    denegar_solicitudes.short_description = "Denegar solicitudes seleccionadas"



