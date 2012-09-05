# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from datetime import datetime

from ateliers_a.main_site.models    import *

from constance import config

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
        'texte_accueil' : config.Accueil,
        'date'          : config.Date,
        'displayDate'   : config.AfficherDate,
        'request'       : request,

    }
    return render_to_response('2-agence.html',
                              arguments,
                              context_instance=RequestContext(request))

def portfolio(request):
    # View limits displaying of 6 items, 6 first chosen

    books = Book.objects.all()
    arguments = {
        'pageN'         : 'portfolio',
#        'pageFlip'      : 'nope',
        'request'       : request,
        'books'         : books,
#        'book1'         : books[1],
#        'book2'         : books[2],
#        'book3'         : books[3],
#        'book4'         : books[4],
#        'book5'         : books[5],
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