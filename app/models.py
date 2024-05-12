from django.db import models


class Cars(models.Model):
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cars'


class Service(models.Model):
    work = models.TextField(blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service'


class Users(models.Model):
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
