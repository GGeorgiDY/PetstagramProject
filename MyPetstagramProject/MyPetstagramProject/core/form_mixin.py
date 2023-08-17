# правейки долното, когато натиснем delete pet и ни се отвори прозорчето, където трябва да потвърдим дали да
# изтрием домашния любимец, всички полета (pet name, date of birth и link to image) ще бъдат readonly и никой
# няма да може да ги променя. В самата PetDeleteForm-а която наследява този клас, описваме кои полета искаме да
# са disabled-ати, като трябва да вземем и __init__ метода.
class DisabledFormMixin:
    disabled_fields = ()
    fields = {}

    def _disable_fields(self):
        if self.disabled_fields == '__all__':
            fields = self.fields.keys()
        else:
            fields = self.disabled_fields

        for field_name in fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'
