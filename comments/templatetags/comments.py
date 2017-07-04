
from django import template

from ..forms import CommentForm


register = template.Library()


@register.inclusion_tag('comments/index.html', takes_context=True)
def render_comments(context, content_type, object_id):

    initial = {'content_type': content_type, 'object_id': object_id}

    form = CommentForm(context.request, initial=initial)

    return {
        'content_type': content_type,
        'object_id': object_id,
        'form': form
    }
