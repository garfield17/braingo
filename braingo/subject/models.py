from django.db import models

class Subjects(models.Model):
    name = models.CharField("Название", max_length=100, null=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"
        db_table = "subjects"