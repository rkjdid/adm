# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from ateliers_a.main_site.models    import *

from django.core import serializers


#def base(request):
#    True


def index(request):
#    base(request)
    arguments = {
        'pageN'         : 'index',
#        'pageFlip'      : 'nope',
        'request'       : request,
    }
    return render_to_response('1-index.html',
                              arguments,
                              context_instance=RequestContext(request))

def agence(request):
#    base(request)
    arguments = {
        'pageN'         : 'agence',
#        'pageFlip'      : 'nope',
        'request'       : request,
    }
    return render_to_response('2-agence.html',
                              arguments,
                              context_instance=RequestContext(request))

def portfolio(request):
#    base(request)
    books = Book.objects.all()
    arguments = {
        'pageN'         : 'portfolio',
#        'pageFlip'      : 'nope',
        'request'       : request,
        'books'         : books,
    }
    return render_to_response('3-portfolio.html',
                              arguments,
                              context_instance=RequestContext(request))

def equipe(request):
#    base(request)
    members = MembreEquipe.objects.all();
    arguments = {
        'pageN'         : 'equipe',
        'members'       : members,
#        'pageFlip'      : 'nope',
        'request'       : request,
    }
    return render_to_response('4-equipe.html',
                              arguments,
                              context_instance=RequestContext(request))

def clients(request):
#    base(request)
    catClients = CategorieClient.objects.all()
#    tvURL = "http://192.168.1.253/ateliers.media/resources/img.pdf/tv+lcd-450.png"
#    tvURL = "http://192.168.1.253/ateliers.media/books/orange.png"
#    tvURL = "/static/img/tv.empty.png"
#    catClientsJSON = serializers.serialize('json', catClients)
    arguments = {
        'pageN'      : 'clients',
        'catClients'     : catClients,
#        'catClientsJSON' : catClientsJSON,
#        'tvURL'      : tvURL,
#        'pageFlip'   : 'nope',
        'request'    : request,
    }

    return render_to_response('5-clients.html',
                              arguments,
                              context_instance=RequestContext(request))

def contact(request):
#    base(request)
    contact = Contact.objects.all()
    arguments = {
        'pageN'         : 'contact',
#        'pageFlip'      : 'flip',
        'request'       : request,
        'contacts'      : contact,
    }
    return render_to_response('6-contact.html',
                              arguments,
                              context_instance=RequestContext(request))