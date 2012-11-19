from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext

from adm.models    import *

def index(request):
    members = MembreEquipe.objects.filter(position__gt = 0)

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

def portfolio(request, pagebookId='-1'):
    books = Book.objects.all()
    pageBook = None

    if pagebookId != '-1':
        try:
            pageBook = PageBook.objects.get(id=pagebookId)
        except PageBook.DoesNotExist:
            return redirect('/portfolio', context_instance=RequestContext(request))

    arguments = {
        'pageN'         : 'portfolio',
        'request'       : request,
        'books'         : books,
        'pbook'         : pageBook,
    }
    return render_to_response('3-portfolio.html',
                              arguments,
                              context_instance=RequestContext(request))

def equipe(request):
    members = MembreEquipe.objects.filter(position__gt = 0)
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

def redirectHome(request):
    return redirect('/', context_instance=RequestContext(request))