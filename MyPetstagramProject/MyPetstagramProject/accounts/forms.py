from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'  # тук казваме какво допълнително искаме да се изисква при регистрация
        field_classes = {"username": auth_forms.UsernameField}


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")      # тук казваме какво допълнително искаме да се изисква при регистрация
        field_classes = {"username": auth_forms.UsernameField}
