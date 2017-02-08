from django.utils import simplejson
from dajaxice.decorators import dajaxice_functions
from dajax.core import Dajax

from models import PageBook, Book

def getImage(request, selector, book, page, bEven):
    if bool(bEven):
        page = Book.objects.all()[int(book)].pagebooks.all()[int(page)].pageGauche.url
    else:
        page = Book.objects.all()[int(book)].pagebooks.all()[int(page)].pageDroite.url

    dajax = Dajax()
    dajax.script('ajaxOnLoad("'+selector+'", "'+page+'", $("#'+selector+'"));')

    return dajax.json()

dajaxice_functions.register(getImage, method='GET')
