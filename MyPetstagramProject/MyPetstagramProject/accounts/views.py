from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model, login
from MyPetstagramProject.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    # model = UserModel                     # грешно - използвай формата вместо това
    # fields = ('username', 'password')     # грешно - използвай формата вместо това
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')    # като се logout-нем къде искаме да отидем


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    # искаме да добавим допълниелни неща в контекста. Това го правим така:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        # self.request.user е логнатия юзър
        # self.object е селектирания юзър
        context['pets_count'] = self.object.pet_set.count()   # вземи броя на животните, които потребителя има
        context['photos_count'] = self.object.photo_set.count()   # вземи броя на снимките, които потребителя има

        # Photo.objects.select_related()  # взима тези обекти които имат foreign key към текущия обект. Връща QuerrySet
        # Photo.objects.prefetch_related()    # взими свързаните по foreign key неща. Използва се за Many-to-one и many-to-many релации.

        photos = self.object.photo_set.prefetch_related('photolike_set')   # prefech_related казва аз ще използвам photos, но ти ми подготви и related нещата по foreign key. Това се прави с цел да имаме по-малко заявки към базата
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)    # за всичките photos да им вземещ техните photolikes предварително

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'username', 'gender', 'email')

    # долното пренасочване го правим динамично заради "pk".
    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
