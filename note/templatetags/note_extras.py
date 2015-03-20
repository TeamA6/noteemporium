from django import template
from note.models import Subject

register = template.Library()

@register.inclusion_tag('noteemp/subs.html')
def get_subject_list():
    return {'subs': Subject.objects.all()}