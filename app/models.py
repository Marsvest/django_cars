from django.db import models


class Users(models.Model):
    name = models.TextField(blank=True, null=True)
    car_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'

    @classmethod
    def get_all_users(cls):
        return cls.objects.all()
