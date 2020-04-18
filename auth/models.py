from django.db import models


class User(models.Model):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table_name = 'auth_user'

    name = models.BooleanField(verbose_name='hello')
