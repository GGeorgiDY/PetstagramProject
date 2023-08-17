def apply_likes_count(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo
    # photolike_set е поле което се създава автоматично, защото имаме модел PhotoLike, който има ForeignKey към Photo модела.
    # тук се следва принципа field in relation is {NAME_OF_THIS_MODEL}_set
    # Photo's field for likes is named '{NAME_OF_THIS_MODEL.lower()}_set'


def apply_user_liked_photo(photo):
    # TODO: fix this for current user when authentication is available
    photo.is_liked_by_user = photo.likes_count > 0
    return photo
