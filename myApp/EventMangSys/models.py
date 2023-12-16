from django.db import models

# Create your models here.
class admins(models.Model):
    name = models.CharField('admin_name',max_length=20)
    email = models.CharField('admin_email',max_length=50)
    contact = models.CharField('admin_pass',max_length=50)
    category = models.CharField('admin_catogary',max_length=20)

