##-*- coding: utf-8 -*-
from django.db import models
from main_site.widgets import AdminImageWidget
from django.db.models.signals import post_save, pre_save
import settings

###################################################################
#-Page CONTACT----------------------------------------------------
###################################################################
class Contact (models.Model):
    """
    Contacts (page CONTACT)
    """
    nom = models.CharField (max_length=50, default='Personne à contacter')

    # Numéro(s) de contact, contact2 facultatif
    contact1 = models.CharField (max_length=50, default='Tel')
    contact2 = models.CharField (max_length=50, null=True)

    def __unicode__(self):
        return self.nom

###################################################################
#-Page CLIENT----------------------------------------------------
###################################################################
class CategorieClient (models.Model):
    """
    Catégories de clients, à droite de la TV (page CLIENT)
    """
    nom = models.CharField (max_length=20, default='Catégorie client')

    def __unicode__(self):
        return self.nom

class Client (models.Model):
    """
    Clients des AdM dans la TV (page CLIENT)
    """
    categorie = models.ForeignKey('CategorieClient', related_name='clients')

    nom = models.CharField (max_length=20, default='Client')

    logo = models.ImageField(upload_to= settings.MEDIA_ROOT + 'clients/')
    logoURL = models.CharField(max_length=150, default=settings.MEDIA_URL + 'clients/')

    def setImgURL(self):
        self.logoURL += self.logo.name

    def __unicode__(self):
        return self.nom

###################################################################
#-Page EQUIPE----------------------------------------------------
###################################################################
class MembreEquipe (models.Model):
    """
    Salariés des AdM (page EQUIPE)
    """
    nom = models.CharField (max_length=20, default='Prenom Nom')
    statut = models.CharField (max_length=20, default='Salarié')

    description = models.TextField(default='Parcours du salarié')

    def __unicode__(self):
        return self.nom

class PhotoMembre (models.Model):
    """
    Photo (photomaton) des membres (page EQUIPE)
    """
    membre = models.ForeignKey('MembreEquipe', related_name='photos')

    photo = models.ImageField(upload_to= settings.MEDIA_ROOT + 'equipe/')
    photoURL = models.CharField(max_length=150, default= settings.MEDIA_URL + 'equipe/')

    def setImgURL(self):
        self.photoURL += self.photo.name

    def __unicode__(self):
        return self.photo.path


###################################################################
#-Page PORTFOLIO---------------------------------------------------
###################################################################
class Book (models.Model):
    """
    Secteur d'activité, book (page PORTFOLIO)
    """
    theme = models.CharField(max_length=75)

    def __unicode__(self):
        return self.theme

class PageBook (models.Model):
    """
    Double page du book, correspondant à un secteur (fiche recette)
    """
    book = models.ForeignKey('Book', related_name='pagebook')

    pageGauche = models.ImageField(upload_to= settings.MEDIA_ROOT + 'books/')
    pageGaucheURL = models.CharField(max_length=150, default=settings.MEDIA_URL + 'books/')
    pageDroite = models.ImageField(upload_to= settings.MEDIA_ROOT + 'books/')
    pageDroiteURL = models.CharField(max_length=150, default=settings.MEDIA_URL + 'books/')

#    def setImgURL(self):
#        self.pageGaucheURL += self.pageGauche.name
#        self.pageDroiteURL += self.pageDroite.name

    def __unicode__(self):
        return self.pageDroiteURL

class FicheRecette (models.Model):
    """
    Recette des ateliers (page PORTFOLIO)
    """
    book = models.OneToOneField('Book', related_name='fiche')

    imagefond = models.ImageField(upload_to= settings.MEDIA_ROOT + 'fichesRecette/')
    imagefondURL = models.CharField(max_length=150, default=settings.MEDIA_URL + 'fichesRecette/')

    titre = models.CharField(max_length=100, default='La recette du bonheur')
    description = models.TextField(default="Faire l'amour")

#    def setImgURL(self):
#        self.imagefondURL += self.imagefond.name

    def __unicode__(self):
        return self.titre

###################################################################
#-Signaux----------------------------------------------------------
###################################################################

#def buildImgURL(sender, instance, **kwargs):
#    if (instance.b_setURL):
#        instance.setImgURL()
#        instance.b_setURL = False
#
#    instance.save()
#
## Build image URLs before saving
#post_save.connect(buildImgURL, sender=PageBook)
#post_save.connect(buildImgURL, sender=Client)
#post_save.connect(buildImgURL, sender=FicheRecette)
#post_save.connect(buildImgURL, sender=PageBook)
