from django.db import models

class Users(models.Model):
    name = models.CharField("Имя", max_length=10000, null=True)
    birthdate = models.DateField("Год рождения", null=True)
    password = models.CharField("Пароль", max_length=10000, null=True)
    email = models.EmailField("Почта", max_length=10000, null=True)
    profile_picture = models.ImageField(upload_to='', null=True, blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        db_table = "accounts"