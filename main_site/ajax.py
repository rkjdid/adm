from django.utils import simplejson
from dajaxice.decorators import dajaxice_register, dajaxice_functions
from dajax.core import Dajax

from models import PageBook

@dajaxice_register(method='GET')
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})

def getImage(request, selector, pageId, bEven):
    dajax = Dajax()

    if bool(bEven):
        page = PageBook.objects.get(id=int(pageId)).pageGauche.url
    else:
        page = PageBook.objects.get(id=int(pageId)).pageDroite.url

    dajax.assign('#' + selector, 'innerHTML', page)

    return dajax.json()

#def getImage(request, id):
##    if bool(bEven):
##        page = PageBook.objects.get(int(pageId)).pageGauche.url
##    else:
##        page = PageBook.objects.get(int(pageId)).pageDroite.url
#    return simplejson.dumps({'pageURL':id})

dajaxice_functions.register(getImage, method='GET')
