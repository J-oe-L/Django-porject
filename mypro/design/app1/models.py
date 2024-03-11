from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to="app1/image",null=True,blank=True)
    def __str__(self):
        return self.name


class team(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to="app1/image",null=True,blank=True)

    def __str__(self):
        return self.name