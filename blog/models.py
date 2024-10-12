from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
# Create your models here.




class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=self.model.Status.PUBLISHED)
    


class Post(models.Model):
    
    # Este es el administrador predeterminado de Django que maneja todas las consultas,
    # permitiendo hacer cosas como Post.objects.all() para obtener todos los objetos.
    objects = models.Manager()

    # Este es un administrador personalizado que hemos creado (PublishedManager),
    # que recupera solo las publicaciones con el estado de "publicado".
    # Te permite hacer consultas como Post.published.all() para obtener solo
    # los posts publicados.
    published = PublishedManager()
    
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
    
    
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish' ) # el slug ayuda a crear url amigables con el seo 
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now) # se pueden usar funciones generadas por las base de datos la cual seria haciendo esta importacion from django.db.model.functions  import Now y luego usando esta funcion "db_default=Now()""
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT) 
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    
    class Meta:
        ordering = ('-publish',)  # - significa que los resultados se ordenaran en orden descendiente según el campo publish
        indexes = [
            models.Index(fields=['-publish']),  # se crea un indice para el campo publish para optimizar las consultas
        ]
    
    def __str__(self):
        return self.title
    
    def get_adsolute_url(self):
        return reverse (
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                  ]
        )
        
        
        
        
        
        
        
        """
                Esta función crea un url absoluto para este post.
        Esto se utiliza para crear enlaces a los posts en el template.
        La función reverse se utiliza para obtener la url de un nombre de vista y sus argumentos.
        
        """
    
    
    
    
        """
        Django trae una forma de autenticar usuarios que viene con la importacion de django.contrib.auth y contiene una clase de modelo User, tambien se puede utilizar AUTH_USER_MODEL que viene de la importacion de django.conf import settings, esta configuracion apunta al auth.User de forma predeterminanda esto es mejor si modificas la clase User que viene por defecto en django.
        """