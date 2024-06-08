import os
import django
from django.utils.text import slugify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotesitedjango.settings")
django.setup()


from quotes.models import Author  # noqa


authors = Author.objects.all()


for author in authors:
    author.slug = slugify(author.fullname)
    author.save()
