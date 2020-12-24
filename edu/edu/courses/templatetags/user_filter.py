from django import template

register = template.Library()


@register.filter(name="filter_for_user")
def filter_for_user(model, user):
    object = model.filter(user=user).select_related()
    if object.count() > 0:
        return object
    else:
        return None
