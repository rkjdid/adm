from adm import settings
from adm.models import *
from django.contrib import admin

class CommonMedia:
    js = (
        'http://ajax.googleapis.com/ajax/libs/dojo/1.8.0/dojo/dojo.js',
        settings.STATIC_URL + 'admin/js/editor.js',
    )
    css = {
        'all': (settings.STATIC_URL + 'admin/css/editor.css',),
    }

class PhotoMembreInline(admin.StackedInline):
    model = PhotoMembre
    extra = 4
    max_num = 4


class MembreEquipeAdmin(admin.ModelAdmin):
    fields = ['nom', 'statut', 'description', 'position']
    list_display = ['nom', 'statut', 'position', 'description']
    list_display_links = ['nom']
    list_editable = ['statut', 'position', 'description']
    inlines = [PhotoMembreInline]


class ClientInline(admin.StackedInline):
    model = Client
    fields = ['nom', 'logo', 'pagebook']
    extra = 1


class CategorieClientAdmin(admin.ModelAdmin):
    fields = ['nom']
    inlines = [ClientInline]

class PageBookInline(admin.StackedInline):
    model = PageBook
    fields = ['pageGauche', 'pageDroite']
    extra = 1

class BookAdmin(admin.ModelAdmin):
    fields = ['theme']
    inlines = [PageBookInline]


admin.site.register(CategorieClient, CategorieClientAdmin)
admin.site.register(MembreEquipe, MembreEquipeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Contact, Media = CommonMedia)
admin.site.register(Accueil, Media = CommonMedia)
