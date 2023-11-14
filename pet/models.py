from django.db import models



from accounts.models import User

# Create your models here.

ESTADOS = (
        ('aceptado', 'Aceptado'),
        ('en_espera', 'En espera'),
        ('denegado', 'Denegado'),
    )

class Pet(models.Model):
    DISPONIBLE = 'Disponible'
    EN_ESPERA = 'En espera'
    ADOPCION = 'Adoptado'

    ESTADO_CHOICES = [
        (DISPONIBLE, 'Disponible'),
        (EN_ESPERA, 'En espera'),
        (ADOPCION, 'Adoptado'),
    ]

    PERRO = 'Perro'
    GATO = 'Gato'

    TIPO_CHOICES = [
        (PERRO, 'Perro'),
        (GATO, 'Gato'),
    ]

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default=DISPONIBLE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    imagen = models.ImageField(upload_to="pets", null=True)

    def __str__(self):
        return self.nombre
    

class SolicitudAdopcion(models.Model):
    

    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_mascota = models.ForeignKey(Pet, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='en_espera')

    # Información adicional del formulario
    nombre_solicitante = models.CharField(max_length=50)
    correo_solicitante = models.EmailField()
    telefono_solicitante = models.CharField(max_length=10)
    direccion_solicitante = models.TextField()
    motivo_solicitud = models.TextField()
    experiencia_mascotas = models.TextField()
    otras_mascotas_en_casa = models.BooleanField()
    espacio_en_casa = models.TextField()

    def __str__(self):
        return f"Solicitud de {self.id_usuario.username} para adoptar a {self.id_mascota.nombre}"
    
    # def save(self, *args, **kwargs):
    #     # Cambiar el estado de la mascota a 'En espera' al guardar la solicitud
    #     self.id_mascota.estado = 'En espera'
    #     self.id_mascota.save()
    #     super().save(*args, **kwargs)
    
    # def aceptar_solicitud(self):
    #     self.estado = 'aceptado'
    #     self.save()

    #     # Cambiar el estado de la mascota a 'Adoptado'
    #     mascota = self.id_mascota
    #     mascota.estado = 'Adoptado'
    #     mascota.save()
    
    # def denegar_solicitud(self):
    #     self.estado = 'denegado'
    #     self.save()

    #     # Cambiar el estado de la mascota a 'Disponible'
    #     mascota = self.id_mascota
    #     mascota.estado = 'Disponible'
    #     mascota.save()


class FormularioVoluntario(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='en_espera')

    # Nuevos campos para el formulario de voluntario
    disponibilidad_tiempo = models.CharField(max_length=255, help_text="¿Cuándo estás disponible para ser voluntario?")
    experiencia_previa = models.TextField(help_text="Describe tu experiencia previa como voluntario o con mascotas.")
    habilidades = models.TextField(help_text="¿Tienes habilidades específicas que puedan ser útiles como voluntario?")
    por_que_voluntario = models.TextField(help_text="Explícanos por qué te gustaría ser voluntario.")

    def __str__(self):
        return f"Solicitud de voluntario de {self.id_usuario.username}"
    
    # def aceptar_solicitud(self):
    #     self.estado = 'aceptado'
    #     self.save()
    
    # def denegar_solicitud(self):
    #     self.estado = 'denegado'
    #     self.save()
        
    








