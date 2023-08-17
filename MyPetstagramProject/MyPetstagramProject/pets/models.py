from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from MyPetstagramProject.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_NAME = 30

    # сложих null=False и blank=False понеже имам изискването това да са задължителни полета за попълване
    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    # това трябва да е линк
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


    # задаваме автоматично да се прави слъг, при добавяне на домашен любимец
    # save е метод, който се извиква автоматично когато се създава или променя домашен любимец.
    # Ние пренаписваме този метод save.
    def save(self, *args, **kwargs):   # взимаме му всички *args и **kwargs, защото те не ни интересуват
        super().save(*args, **kwargs)   # записваме го в базата от данни за да може после да му вземем id-то

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)    # пак го записваме в базата от данни