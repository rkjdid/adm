# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from ateliers_a.main_site.models    import *

def index(request):
    members = MembreEquipe.objects.all();

    arguments = {
        'pageN'         : 'index',
        'request'       : request,
        'membres'       : members,
    }
    return render_to_response('1-index.html',
                              arguments,
                              context_instance=RequestContext(request))

def agence(request):
    news = Accueil.objects.all()
    arguments = {
        'pageN'         : 'agence',
        'news'          : news,
        'request'       : request,
    }
    return render_to_response('2-agence.html',
                              arguments,
                              context_instance=RequestContext(request))

def portfolio(request):
    books = Book.objects.all()
    arguments = {
        'pageN'         : 'portfolio',
        'request'       : request,
        'books'         : books,
    }
    return render_to_response('3-portfolio.html',
                              arguments,
                              context_instance=RequestContext(request))

def equipe(request):
    members = MembreEquipe.objects.all();
    arguments = {
        'pageN'         : 'equipe',
        'members'       : members,
        'request'       : request,
    }
    return render_to_response('4-equipe.html',
                              arguments,
                              context_instance=RequestContext(request))

def clients(request):
    catClients = CategorieClient.objects.all()
    arguments = {
        'pageN'      : 'clients',
        'catClients' : catClients,
        'request'    : request,
    }

    return render_to_response('5-clients.html',
                              arguments,
                              context_instance=RequestContext(request))

def contact(request):
    contact = Contact.objects.all()
    arguments = {
        'pageN'         : 'contact',
        'request'       : request,
        'contacts'      : contact,
    }
    return render_to_response('6-contact.html',
                              arguments,
                              context_instance=RequestContext(request))