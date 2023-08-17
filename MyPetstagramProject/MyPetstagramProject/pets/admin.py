from django.contrib import admin
from MyPetstagramProject.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

