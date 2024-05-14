from django.db import models


class Cars(models.Model):
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True, unique=True)
    owner = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cars'


class Service(models.Model):
    start_timestamp = models.IntegerField(blank=True, null=True)
    end_timestamp = models.IntegerField(blank=True, null=True)
    oil_work = models.BooleanField(blank=True, null=True)
    fluids_work = models.BooleanField(blank=True, null=True)
    filters_work = models.BooleanField(blank=True, null=True)
    brake_system_work = models.BooleanField(blank=True, null=True)
    suspension_steering_work = models.BooleanField(blank=True, null=True)
    exhaust_work = models.BooleanField(blank=True, null=True)
    tires_work = models.BooleanField(blank=True, null=True)
    lighting_work = models.BooleanField(blank=True, null=True)
    car = models.ForeignKey(Cars, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service'


class Clients(models.Model):
    name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clients'
