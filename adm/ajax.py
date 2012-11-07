from django.utils import simplejson
from dajaxice.decorators import dajaxice_register, dajaxice_functions
from dajax.core import Dajax

from models import PageBook, Book

#@dajaxice_register(method='GET')
#def sayhello(request):
#    return simplejson.dumps({'message':'Hello World'})

#def getImage(request, selector, pageId, bEven):
#    dajax = Dajax()
#
#    if bool(bEven):
#        page = PageBook.objects.all()[int(pageId)].pageGauche.url
#    else:
#        page = PageBook.objects.all()[int(pageId)].pageDroite.url
#
#    tag = "<img class=\"pageBook\" alt=\"Photo book\" src=\"" + page + "\" />"
#
#    dajax.remove('#' + selector + ' .loader')
#    dajax.append('#' + selector, 'innerHTML', tag)
#
#    return dajax.json()

def getImage(request, selector, book, page, bEven):
    dajax = Dajax()

    if bool(bEven):
        page = Book.objects.all()[int(book)].pagebooks.all()[int(page)].pageGauche.url
    else:
        page = Book.objects.all()[int(book)].pagebooks.all()[int(page)].pageDroite.url

    tag = "<img class=\"pageBook\" alt=\"Photo book\" src=\"" + page + "\" />"

    dajax.remove('#' + selector + ' .loader')
    dajax.append('#' + selector, 'innerHTML', tag)

    return dajax.json()

dajaxice_functions.register(getImage, method='GET')
