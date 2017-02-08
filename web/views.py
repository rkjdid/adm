from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from models    import *

def index(request, zoom=100):
    members = MembreEquipe.objects.filter(position__gt = 0)

    arguments = {
        'pageN'         : 'index',
        'request'       : request,
        'membres'       : members,
        'zoom'          : zoom,
    }
    return render_to_response('web/1-index.html',
                              arguments,
                              RequestContext(request))

def agence(request):
    news = Accueil.objects.all()
    arguments = {
        'pageN'         : 'agence',
        'news'          : news,
        'request'       : request,
    }
    return render_to_response('web/2-agence.html',
                              arguments,
                              RequestContext(request))

def portfolio(request, pagebookId='-1'):
    books = Book.objects.all()
    pageBook = None

    if pagebookId != '-1':
        try:
            pageBook = PageBook.objects.get(id=pagebookId)
        except PageBook.DoesNotExist:
            return redirect('/portfolio', RequestContext(request))

    arguments = {
        'pageN'         : 'portfolio',
        'request'       : request,
        'books'         : books,
        'pbook'         : pageBook,
    }
    return render_to_response('web/3-portfolio.html',
                              arguments,
                              RequestContext(request))

def equipe(request):
    members = MembreEquipe.objects.filter(position__gt = 0)
    arguments = {
        'pageN'         : 'equipe',
        'members'       : members,
        'request'       : request,
    }
    return render_to_response('web/4-equipe.html',
                              arguments,
                              RequestContext(request))

def clients(request):
    catClients = CategorieClient.objects.all()
    arguments = {
        'pageN'      : 'clients',
        'catClients' : catClients,
        'request'    : request,
    }

    return render_to_response('web/5-clients.html',
                              arguments,
                              RequestContext(request))

def contact(request):
    contact = Contact.objects.all()
    arguments = {
        'pageN'         : 'contact',
        'request'       : request,
        'contacts'      : contact,
    }
    return render_to_response('web/6-contact.html',
                              arguments,
                              RequestContext(request))

def redirectHome(request):
    return redirect('/', RequestContext(request))

def redirectAgence(request):
    return redirect('/agence/', RequestContext(request))

def redirectPortfolio(request):
    return redirect('/portfolio/', RequestContext(request))

def redirectContact(request):
    return redirect('/contact/', RequestContext(request))
