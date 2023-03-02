import django.db.models

class Users(django.db.models.Model):
    name = django.db.models.CharField("Имя", max_length=10000, null=True, default="TheGreatestBrain")
    last_name = django.db.models.CharField("Фамилия", max_length=10000, null=True)
    birthdate = django.db.models.IntegerField("Год рождения", null=True)
    status = django.db.models.IntegerField("Статус активности", null=True, default=1)
    password = django.db.models.CharField("Пароль", max_length=10000, null=True)
    about = django.db.models.TextField("О себе", max_length=10000, null=True)
    email = django.db.models.EmailField("Почта", max_length=10000, null=True)
    profile_picture = django.db.models.ImageField(upload_to='', null=True, blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
        db_table = "accounts"