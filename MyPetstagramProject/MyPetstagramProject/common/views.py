import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from MyPetstagramProject.common.forms import PhotoCommentForm, SearchPhotosForm
from MyPetstagramProject.common.models import PhotoLike
from MyPetstagramProject.common.utils import get_photo_url
from MyPetstagramProject.core.photo_utils import apply_likes_count, apply_user_liked_photo
from MyPetstagramProject.photos.models import Photo


def index(request):
    search_form = SearchPhotosForm(request.GET)   # слагаме го заради search формата
    search_pattern = None
    if search_form.is_valid():   # правим го за да ни се попълни информацията която я имаме
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()  # слагаме го заради search формата
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)
    # горните редове са за ssearch box-a

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
        'comment_form': PhotoCommentForm(),
        'search_form': search_form,
    }

    return render(request, 'common/home-page.html', context)


@login_required
def like_photo(request, photo_id):
    user_liked_photos = PhotoLike.objects.filter(photo_id=photo_id, user_id=request.user.pk)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # create създава обект с **kwargs и го извиква
        PhotoLike.objects.create(
            photo_id=photo_id,
            user_id=request.user.pk,
        )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))


@login_required
def comment_photo(request, photo_id):
    photo = Photo.objects.filter(pk=photo_id).get()
    # тук не е необходимо да си правим if == GET понеже тук имаме само POST метод
    form = PhotoCommentForm(request.POST)

    # ако е валидна формата, тогава запази коментара
    if form.is_valid():
        # правейки го по този начин
        comment = form.save(commit=False)   # does not persist to DB
        comment.photo = photo
        comment.save()

    return redirect('index')