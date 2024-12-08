from django.forms.widgets import SelectMultiple
from .models import Tag

class TagWidget(SelectMultiple):
    """
    Custom multi-select widget to render tags dynamically.
    """

    def __init__(self, attrs=None):
        # Set tag options dynamically for rendering
        tag_choices = [(tag.id, tag.name) for tag in Tag.objects.all()]
        super().__init__(attrs, choices=tag_choices)

    def value_from_datadict(self, data, files, name):
        # Return a list of tag IDs
        return data.getlist(name)