from django import template
from courses.models import StudentModuleTestStatus, StudentAnswer

register = template.Library()


@register.filter(name="filter_for_user")
def filter_for_user(model, user):
    object = model.filter(user=user).select_related()
    if object.count() > 0:
        return object
    else:
        return None


@register.filter(name="filter_object_for_user")
def filter_for_user(model, user):
    try:
        query_object = model.get(user=user)
        return query_object
    except:
        return None


@register.filter(name="test_is_passed")
def test_is_passed(module_test, user):
    print("ID", module_test.id)

    return StudentModuleTestStatus.objects.get(module_test=module_test, user=user).passed


@register.filter(name="get_student_answers_for_user")
def get_student_answers_for_user(input_queryset, user):
    try:

        queryset = input_queryset.filter(user=user).select_related('answer')
        return queryset
    except:
        return None


@register.filter(name="get_student_answer_for_user")
def get_student_answer_for_user(question, user):
    try:
        query_object = StudentAnswer.objects.select_related('answer').get(user=user, question=question)
        return query_object
    except StudentAnswer.DoesNotExist:
        return None
