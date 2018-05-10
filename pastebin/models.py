from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LANG_CHOICES = sorted([(item[1][0], item[0]) for item in [item for item in get_all_lexers() if item[1]]])

class Paste(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100, choices=LANG_CHOICES)
    code_body = models.TextField()
