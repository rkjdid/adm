from ateliers_a.main_site.models import *
from django.contrib import admin

class PhotoMembreInline(admin.StackedInline):
    model = PhotoMembre
    extra = 4
    max_num = 4


class MembreEquipeAdmin(admin.ModelAdmin):
    fields = ['nom', 'statut', 'description', 'position', 'visible']
    list_display = ['nom', 'statut', 'position', 'visible', 'description']
    list_display_links = ['description']
    list_editable = ['nom', 'statut', 'position', 'visible']
    inlines = [PhotoMembreInline]


class ClientInline(admin.StackedInline):
    model = Client
    fields = ['nom', 'logo']
    extra = 1


class CategorieClientAdmin(admin.ModelAdmin):
    fields = ['nom']
    inlines = [ClientInline]

class PageBookInline(admin.StackedInline):
    model = PageBook
    fields = ['pageGauche', 'pageDroite']
    extra = 1

class FicheRecetteInline(admin.StackedInline):
    model = FicheRecette
    fields = ['titre', 'description']

class BookAdmin(admin.ModelAdmin):
    fields = ['theme']
    inlines = [FicheRecetteInline, PageBookInline]


admin.site.register(CategorieClient, CategorieClientAdmin)
admin.site.register(MembreEquipe, MembreEquipeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Contact)
admin.site.register(Accueil)
