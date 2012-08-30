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

# Static dimensions - (logo == logos clients - will be resized)
logoWidth = 110
logoHeight = 84
# Photo membre - won't be resized
# PageBook - won't be resized (232*432)
pagebookWidth = 299
pagebookHeight = 423
#photoMembrme - will be resized
photoMembreWidth = 80
photoMembreHeight = 428


def scaleImg (path, wantedWidth, wantedHeight):
    im = Image.open(path)
    if im.size[0] <= wantedWidth and im.size[1] <= wantedHeight:
        return

    imratio = float(im.size[0]) / float(im.size[1])

    wdiff_h = wantedWidth / imratio
    hdiff_w = wantedHeight * imratio

    if wdiff_h <= wantedHeight:
        im = im.resize((wantedWidth, int(wdiff_h)), Image.ANTIALIAS)
    elif hdiff_w <= wantedWidth:
        im = im.resize((int(hdiff_w), wantedHeight), Image.ANTIALIAS)

    im.save(path)

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
    nom = models.CharField (max_length=75, default='Personne à contacter')

    # Numéro(s) de contact, contact2 facultatif
    contact1 = models.CharField (max_length=75, default='Tel')
    contact2 = models.CharField (max_length=75, default='Mail', blank=True)

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
        scaleImg(self.logo.path, logoWidth, logoHeight)
#        im = Image.open(self.logo.path)
#        if im.size[0] <= logoWidth and im.size[1] <= logoHeight:
#            return
#
#        imratio = float(im.size[0]) / float(im.size[1])
#
#        wdiff_h = logoWidth / imratio
#        hdiff_w = logoHeight * imratio
#
#        if wdiff_h <= logoHeight:
#            im = im.resize((logoWidth, int(wdiff_h)), Image.ANTIALIAS)
#        elif hdiff_w <= logoWidth:
#            im = im.resize((int(hdiff_w), logoHeight), Image.ANTIALIAS)
#
#        im.save(self.logo.path)

    def setImgURL(self):
        _, self.logo.name = uniqueFile(settings.MEDIA_ROOT + 'clients/' + self.logo.name)
        self.logoURL = self.logoURL_base + self.logo.name

    def __unicode__(self):
        return self.nom

###################################################################
#-Page EQUIPE----------------------------------------------------
###################################################################
BUBBLE_POSITION = (
    (0, u'0-Caché'),
    (1, u'1-BasGauche'),
    (2, u'2-Gauche1'),
    (3, u'3-Gauche2'),
    (4, u'4-GaucheHaut'),
    (5, u'5-HautGauche'),
    (6, u'6-Haut'),
    (7, u'7-HautDroite'),
    (8, u'8-DroiteHaut'),
    (9, u'9-Droite1'),
    (10, u'10-Droite2'),
    (11, u'11-BasDroite'),
)

class MembreEquipe (models.Model):
    """
    Salariés des AdM (page EQUIPE)
    """
    nom = models.CharField (max_length=30, default='Prenom Nom')
    statut = models.CharField (max_length=30, default='Job title')

    visible = models.BooleanField (default=True)
    position = models.IntegerField (default=None, choices=BUBBLE_POSITION, null=True)
    description = models.TextField(default='Parcours personnel')

    def __unicode__(self):
        return self.nom

class PhotoMembre (models.Model):
    """
    Photo (photomaton) des membres (page EQUIPE)
    """
    membre = models.OneToOneField('MembreEquipe', related_name='photo')

    photo = models.ImageField(upload_to='equipe/')
    photoURL_base = models.CharField(editable=False, max_length=150, default= settings.MEDIA_URL + 'equipe/')
    photoURL = models.CharField(editable=False, max_length=150)

    def setImgURL(self):
        _, self.photo.name = uniqueFile(settings.MEDIA_ROOT + 'equipe/' + self.photo.name)
        self.photoURL = self.photoURL_base + self.photo.name

    def resizeImg(self):
        scaleImg(self.photo.path, photoMembreWidth, photoMembreHeight)

    def __unicode__(self):
        return self.photo.path


###################################################################
#-Page PORTFOLIO---------------------------------------------------
###################################################################
class Book (models.Model):
    """
    Pole d'activité, book (page PORTFOLIO)
    """
    theme = models.CharField(max_length=75)

    def __unicode__(self):
        return self.theme

class PageBook (models.Model):
    """
    Double page du book, correspondant à un secteur (fiche recette)
    """

    book = models.ForeignKey('Book', related_name='pagebooks')

    pageGauche = models.ImageField(upload_to='books/')
    pageDroite = models.ImageField(upload_to='books/')
    pageGauche.short_description = 'Page Gauche (299*423)px'
    pageDroite.short_description = 'Page Droite (299*423)px'

    pageGaucheURL = models.CharField(editable=False, max_length=150)
    pageDroiteURL = models.CharField(editable=False, max_length=150)
    pageURL_base = models.CharField(editable=False, default=settings.MEDIA_URL + 'books/', max_length=150)

    def resizeImg(self):
        scaleImg(self.pageGauche.path, pagebookWidth, pagebookHeight)
        scaleImg(self.pageDroite.path, pagebookWidth, pagebookWidth)

#        im = Image.open(self.pageGauche.path)
#        if im.size[0] <= pagebookWidth and im.size[1] <= logoHeight:
#            return
#
#        imratio = float(im.size[0]) / float(im.size[1])
#
#        wdiff_h = pagebookWidth / imratio
#        hdiff_w = pagebookHeight * imratio
#
#        if wdiff_h <= pagebookHeight:
#            im = im.resize((pagebookWidth, int(wdiff_h)), Image.ANTIALIAS)
#        elif hdiff_w <= pagebookWidth:
#            im = im.resize((int(hdiff_w), pagebookHeight), Image.ANTIALIAS)
#
#        im.save(self.pageGauche.path)

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

    #    imagefond = models.ImageField(upload_to= settings.MEDIA_ROOT + 'fichesRecette/')
    #    imagefondURL_base = models.CharField(editable=False, max_length=150, default=settings.MEDIA_URL + 'fichesRecette/')
    #    imagefondURL = models.CharField(editable=False, max_length=150)
    titre = models.CharField(max_length=100, default='titre fiche')
    description = models.TextField(default="description fiche (recette 100g..)")

#    def setImgURL(self):
#        _, self.imagefond.name = uniqueFile(settings.MEDIA_ROOT + 'fichesRecette/' + self.imagefond.name)
#        self.imagefondURL = self.imagefondURL_base + self.imagefond.name

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
#pre_save.connect(buildImgURL, sender=FicheRecette)
pre_save.connect(buildImgURL, sender=PageBook)
pre_save.connect(buildImgURL, sender=PhotoMembre)

#post_save.connect(buildImgURL, sender=PageBook)
post_save.connect(resizeImg, sender=Client)
post_save.connect(resizeImg, sender=PageBook)
post_save.connect(resizeImg, sender=PhotoMembre)
#post_save.connect(buildImgURL, sender=FicheRecette)
#post_save.connect(buildImgURL, sender=PageBook)
