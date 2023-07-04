from django.db import models
from django.urls import reverse

# Create your models here.
class Branches(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='branch',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='branch'
        verbose_name_plural='branches'

    def get_url(self):
        return reverse('bankapp:branches_by_places',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Places(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    branch=models.ForeignKey (Branches,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='place',blank=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('bankapp:placecatdetail', args=[self.branch.slug, self.slug])


    class Meta:
        ordering = ('name',)
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return '{}'.format(self.name)