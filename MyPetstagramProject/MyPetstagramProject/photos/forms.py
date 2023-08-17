from django import forms
from django.core.exceptions import ValidationError
from MyPetstagramProject.common.models import PhotoLike, PhotoComment
from MyPetstagramProject.core.form_mixin import DisabledFormMixin
from MyPetstagramProject.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'location', 'tagged_pets', )


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('photo', 'publication_date')


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = ('photo', 'description', 'location', 'tagged_pets')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()   # така трием many-to-many тагнатите животни

            PhotoLike.objects.filter(photo_id=self.instance.id).delete()    # така трием one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()   # така трием one-to-many
            self.instance.delete()

        return self.instance
