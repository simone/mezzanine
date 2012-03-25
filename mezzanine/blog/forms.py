
from django import forms

from mezzanine.blog.models import BlogPost
from mezzanine.core.models import CONTENT_STATUS_DRAFT


class BlogPostForm(forms.ModelForm):
    """
    Model form for ``BlogPost`` that provides the quick blog panel in the
    admin dashboard.
    """

    class Meta:
        model = BlogPost
        fields = ("title", "content", "status", "gen_description")

    def __init__(self):
        initial = {"status": CONTENT_STATUS_DRAFT, "gen_description": True}
        super(BlogPostForm, self).__init__(initial=initial)
        self.fields["status"].widget = forms.HiddenInput()
        self.fields["gen_description"].widget = forms.HiddenInput()
