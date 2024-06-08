
from django import template
from ..models import Author, Quote
register = template.Library()


def get_author(id_):
        author = Author.objects.get(pk=id_)
        return author.fullname

def get_quotes():
        quotes = Quote.objects.all()
        return quotes


