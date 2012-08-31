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
    fields = ['nom', 'logo']#, 'logoURL']
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

class AccueilAdmin(admin.ModelAdmin):
    fields = ['content']
    max_num = 1
    extra = 0


admin.site.register(CategorieClient, CategorieClientAdmin)
admin.site.register(MembreEquipe, MembreEquipeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Contact)
admin.site.register(Accueil, AccueilAdmin)






#
#class UserProfileAdmin(admin.ModelAdmin):
#    fields = ['user', 'gender', 'birthdate', 'first_connexion']
#    inlines = [ProfilePictureInline]

#class ProfilePictureInline(admin.StackedInline):
#    model = UserProfilePicture
#    fk_name = 'user'
#
#class UserProfileAdmin(admin.ModelAdmin):
#    fields = ['user', 'gender', 'birthdate', 'first_connexion']
#    inlines = [ProfilePictureInline]
#
#admin.site.register(UserProfile, UserProfileAdmin)
#
#class WallMsgInline (admin.TabularInline):
#    model = WallMsg
#    extra = 1
#
#class WallAdmin (admin.ModelAdmin):
#    inlines = [WallMsgInline]
#
#admin.site.register(Wall, WallAdmin)
#
#class EventPicturesInline(admin.StackedInline):
#    model = EventPicture
#    extra = 1
#
#class EventAttendanceInline(admin.TabularInline):
#    model = EventAttendance
#    extra = 1
#
#class TagAttachementInline(admin.TabularInline):
#    model = TagAttachement
#    extra = 1
#
#class EventAdmin(admin.ModelAdmin):
#    fields = ['name', 'description', 'category', 'start_time', 'end_time', 'confidentiality', ]
#    inlines = [TagAttachementInline, EventPicturesInline, EventAttendanceInline]
#
#admin.site.register(Event, EventAdmin)