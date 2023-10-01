from django.db import models
from django.utils import timezone, text
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = text.slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model) :
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    class Pin(models.TextChoices):
        PIN = 'PI', 'Pin'
        UNPIN = 'UN', 'Unpin'
    title = models.CharField(max_length = 250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length = 250, unique=True, editable=False)
    img = models.ImageField(upload_to='images/', default="")
    body = RichTextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    pin = models.CharField(max_length=2, choices=Pin.choices, default=Pin.UNPIN)

    def get_absolute_url(self):
        kwargs = {
            'pk' : self.id,
            'slug' : self.slug
        }
        return reverse("blog_detail", kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = text.slugify(value, allow_unicode=True)
        super().save(*args, *kwargs)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]
    def __str__(self):
        return self.title
