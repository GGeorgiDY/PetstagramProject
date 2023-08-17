from django.contrib import admin
from MyPetstagramProject.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'pets')

    # в админ панела за всяка снимка да ми изброи със запетая тагнатите животни
    @staticmethod
    def pets(current_photo_obj):
        tagged_pets = current_photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No pets'
