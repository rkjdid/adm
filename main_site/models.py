##-*- coding: utf-8 -*-

from django.db import models
#from main_site.widgets import AdminImageWidget
from django.db.models.signals import  post_save, pre_save

# PIL resizing
#import urllib
from PIL import Image

# File saving
import os
import tempfile

# Settings
from ateliers_a import settings

# Static dimensions
logoWidth = 110
logoHeight = 84

#photo



###################################################################
#-Général----------------------------------------------------
###################################################################
#def resize (image, max_height, max_width):
#    im = Image.open(urllib.urlopen())

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

    logo = models.ImageField(upload_to= 'clients/')
    logoURL_base = models.CharField(editable=False, max_length=150, default=settings.MEDIA_URL + 'clients/')
    logoURL = models.CharField(editable=False, max_length=150)

    def resizeImg(self):
        im = Image.open(self.logo.path)
        if im.size[0] <= logoWidth and im.size[1] <= logoHeight:
            return

        imratio = float(im.size[0]) / float(im.size[1])

        wdiff_h = logoWidth / imratio
        hdiff_w = logoHeight * imratio

#        imrsz = None

        if wdiff_h <= logoHeight:
            im = im.resize((logoWidth, int(wdiff_h)), Image.ANTIALIAS)
        elif hdiff_w <= logoWidth:
            im = im.resize((int(hdiff_w), logoHeight), Image.ANTIALIAS)

#        im.

#        os.remove(self.logo.path)
        im.save(self.logo.path)

    def setImgURL(self):
        _, self.logo.name = uniqueFile(settings.MEDIA_ROOT + 'clients/' + self.logo.name)
        self.logoURL = self.logoURL_base + self.logo.name

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

    photo = models.ImageField(upload_to='equipe/')
    photoURL_base = models.CharField(editable=False, max_length=150, default= settings.MEDIA_URL + 'equipe/')
    photoURL = models.CharField(editable=False, max_length=150)

    def setImgURL(self):
        _, self.photo.name = uniqueFile(settings.MEDIA_ROOT + 'equipe/' + self.photo.name)
        self.photoURL = self.photoURL_base + self.photo.name

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

    pageGauche = models.ImageField(upload_to='books/')
    pageDroite = models.ImageField(upload_to='books/')

    pageGaucheURL = models.CharField(editable=False, max_length=150)
    pageDroiteURL = models.CharField(editable=False, max_length=150)
    pageURL_base = models.CharField(editable=False, default=settings.MEDIA_URL + 'books/', max_length=150)

    def setImgURL(self):
        _, self.pageGauche.name = uniqueFile(settings.MEDIA_ROOT + 'books/' + self.pageGauche.name)
        _, self.pageDroite.name = uniqueFile(settings.MEDIA_ROOT + 'books/' + self.pageDroite.name)
        self.pageGaucheURL = self.pageURL_base + self.pageGauche.name
        self.pageDroiteURL = self.pageURL_base + self.pageDroite.name

    def __unicode__(self):
        return self.pageDroiteURL

class FicheRecette (models.Model):
    """
    Recette des ateliers (page PORTFOLIO)
    """
    book = models.OneToOneField('Book', related_name='fiche')

    imagefond = models.ImageField(upload_to= settings.MEDIA_ROOT + 'fichesRecette/')
    imagefondURL_base = models.CharField(editable=False, max_length=150, default=settings.MEDIA_URL + 'fichesRecette/')
    imagefondURL = models.CharField(editable=False, max_length=150)
    titre = models.CharField(max_length=100, default='titre')
    description = models.TextField(default="description")

    def setImgURL(self):
        _, self.imagefond.name = uniqueFile(settings.MEDIA_ROOT + 'fichesRecette/' + self.imagefond.name)
        self.imagefondURL = self.imagefondURL_base + self.imagefond.name

    def __unicode__(self):
        return self.titre

###################################################################
#-Divers/Signaux---------------------------------------------------
###################################################################

def uniqueFile(path):
    """
    From path to file :
        returns new_Dir
        returns new_FileName
    """
    dir, fileName = os.path.split(path)
    name, ext = os.path.splitext(fileName)

    fd, newPath = tempfile.mkstemp(ext, name+"_", dir)
    os.close(fd)
    os.remove(newPath)
    dir, fileName = os.path.split(newPath)

    return dir, fileName

def buildImgURL(sender, instance, **kwargs):
    instance.setImgURL()

def resizeImg(sender, instance, **kwargs):
    instance.resizeImg()

## Build image URLs before saving
pre_save.connect(buildImgURL, sender=PageBook)
pre_save.connect(buildImgURL, sender=Client)
pre_save.connect(buildImgURL, sender=FicheRecette)
pre_save.connect(buildImgURL, sender=PageBook)

#post_save.connect(buildImgURL, sender=PageBook)
post_save.connect(resizeImg, sender=Client)
#post_save.connect(buildImgURL, sender=FicheRecette)
#post_save.connect(buildImgURL, sender=PageBook)
