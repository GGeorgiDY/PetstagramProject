from django import forms
from MyPetstagramProject.core.form_mixin import DisabledFormMixin
from MyPetstagramProject.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        # fields = '__all__' # (not the case because we want to skip the 'slug')
        # exclude = ('slug',) # this is the same as below. Тук казваме какво не искаме да се показва.
        fields = ('name', 'date_of_birth', 'personal_photo',) # това използвай - така си изброяваме кои полета искаме да ни се появят и в какъв ред

        # преименуваме имената на полетата в сайта
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }

        # казваме какво да пише като подсказка вътре в полето
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                }
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    # овъррайдваме form.save() от views.py. commit означава дали искаме информацията да се прати към базата.
    # И ако имаме commit, изтриваме информацията. Тоест за тази форма променяме логиката какво значи ти да
    # запазиш една форма.
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance
