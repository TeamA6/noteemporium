from django import template
from note.models import Subject

register = template.Library()

@register.inclusion_tag('noteemp/subs.html')
def get_subject_list(sub=None):
    return {'subs': Subject.objects.all(), 'act_sub': sub}