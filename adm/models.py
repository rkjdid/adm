##-*- coding: utf-8 -*-

from django.db import models
#from adm.widgets import AdminImageWidget
from django.db.models.signals import  post_save, pre_save

# PIL resizing
#import urllib
from PIL import Image

# File saving
import os
import tempfile
from datetime import datetime

#from django.http import

# Static dimensions - (logo == logos clients - will be resized)
logoWidth = 90
logoHeight = 90
# PageBook - will be resized (370*450)
pagebookWidth = 370
pagebookHeight = 450
#photoMembrme - will be resized
photoMembreWidth = 95
photoMembreHeight = 505


###################################################################
#-Page ACCUEIL----------------------------------------------------#
###################################################################
class Accueil (models.Model):
    """
    Accueil (texte)
    """
    class Meta:
#        ordering = ['-date']
        verbose_name_plural = '(p1/Agence) News'

    content = models.TextField (default='Bienvenue sur le site des ateliers des marques(c).')
#    date    = models.DateField (default=datetime.now)
#    author  = models.CharField (max_length=75, default='')
#    display = models.BooleanField (default=True)

    def __unicode__(self):
        return '#' + str(self.id)

###################################################################
#-Page CONTACT----------------------------------------------------#
###################################################################
class Contact (models.Model):
    """
    Contacts (page CONTACT)
    """
    class Meta:
        verbose_name_plural = "(p5/Contact) Contacts"

    nom = models.CharField (max_length=75, default='Personne à contacter')

    # Numéro(s) de contact, contact2 facultatif
    contact1 = models.TextField (default='small info', blank=True, null=True)
    contact2 = models.TextField (default='small info', blank=True, null=True)

    def __unicode__(self):
        return '#' + str(self.id) + '.' + self.nom

###################################################################
#-Page EQUIPE----------------------------------------------------
###################################################################
BUBBLE_POSITION = (
    (0, u'0-Caché'), (1, u'1-Haut'), (2, u'2'),
    (3, u'3'),       (4, u'4'),      (5, u'5'),
    (6, u'6'),       (7, u'7'),      (8, u'8'),
    (9, u'9'),       (10, u'10'),    (11, u'11'),
    (12, u'12'),     (13, u'13'),    (14, u'14'),
    (15, u'15'),     (16, u'16'),    (17, u'17'),
    (18, u'18'),     (19, u'19'),    (20, u'20-Bas'),
)

class MembreEquipe (models.Model):
    """
    Salariés des AdM (page EQUIPE)
    """
    class Meta:
        ordering = ['position']
        verbose_name_plural = "(p3/Equipe) Membres des ateliers"

    nom = models.CharField (max_length=30, default='Prenom Nom')
    statut = models.CharField (max_length=30, default='Job title')

    position = models.IntegerField (default=None, choices=BUBBLE_POSITION, null=True)
    description = models.TextField(default='Parcours personnel')

    def __unicode__(self):
        return '#' + str(self.id) + '.' + self.nom

class PhotoMembre (models.Model):
    """
    Photo (photomaton) des membres (page EQUIPE)
    """
    membre = models.OneToOneField('MembreEquipe', related_name='photo')

    photo = models.ImageField(upload_to= 'equipe/')

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
    class Meta:
        ordering = ['id']
        verbose_name_plural = "(p2/Portfolio) Books"

    theme = models.CharField(max_length=75)

    def nbPages (self):
        return self.pagebooks.count()

    def __unicode__(self):
        return '#' + str(self.id) + '.' + self.theme

class PageBook (models.Model):
    """
    Double page du book, correspondant à un secteur (fiche recette)
    """

    book = models.ForeignKey('Book', related_name='pagebooks')

    pageGauche = models.ImageField(upload_to= 'books/')
    pageDroite = models.ImageField(upload_to= 'books/')
    pageGauche.short_description = 'Page Gauche (299*423)px'
    pageDroite.short_description = 'Page Droite (299*423)px'

    def resizeImg(self):
        scaleImg(self.pageGauche.path, pagebookWidth, pagebookHeight)
        scaleImg(self.pageDroite.path, pagebookWidth, pagebookHeight)

    def __unicode__(self):
        return self.book.theme + ': ' + self.pageGauche.url

###################################################################
#-Page CLIENT----------------------------------------------------
###################################################################
class CategorieClient (models.Model):
    """
    Catégories de clients, à droite de la TV (page CLIENT)
    """
    class Meta:
        verbose_name_plural = "(p4/Clients) Catégories client"

    nom = models.CharField (max_length=20, default='Catégorie client')

    def __unicode__(self):
        return '#' + str(self.id) + '.' + self.nom

class Client (models.Model):
    """
    Clients des AdM dans la TV (page CLIENT)
    """
    categorie = models.ForeignKey('CategorieClient', related_name='clients')
    nom = models.CharField (max_length=20, default='Client', null=True, blank=True)
    logo = models.ImageField(upload_to= 'clients/')

    pagebook = models.OneToOneField('PageBook', related_name="client", blank=True, null=True, on_delete=models.SET_NULL)

    def hasPageBook (self):
        return not (self.pagebook is None)

    def getPageBookID(self):
        if self.hasPageBook():
            return self.pagebook.id
        else:
            return -1

    def resizeImg(self):
        scaleImg(self.logo.path, logoWidth, logoHeight)

    def __unicode__(self):
        return '#' + str(self.id) + '.' + self.nom + '@' + self.categorie.nom

###################################################################
#-Divers/Signaux---------------------------------------------------
###################################################################
def scaleImg (path, wantedWidth, wantedHeight):
    im = Image.open(path)

    if im.size[0] <= wantedWidth and im.size[1] <= wantedHeight:
        return

    imratio = float(im.size[0]) / float(im.size[1])

    wdiff_h = wantedWidth / imratio
    hdiff_w = wantedHeight * imratio

    newIm = None

    if wdiff_h <= wantedHeight:
        newIm = im.convert("RGBA").resize((wantedWidth, int(wdiff_h)), Image.ANTIALIAS)
    elif hdiff_w <= wantedWidth:
        newIm = im.convert("RGBA").resize((int(hdiff_w), wantedHeight), Image.ANTIALIAS)

    # Save resized image
    newIm.save(path)

    # Check if file is a PNG file
    _, ext = os.path.splitext(path)

    # Return if no PNG, no more can be done.
    if ext != '.png':
        return

    # If .png, use tinyPng.org API to compress it, in a thread
    import threading
    threading.Thread(None, tinyCompress, None, (path,)).start()

def tinyCompress (path):
    # NB: api:Z1NUBU0JCIWQcDYoJnzeg33wrUnghzkJ  expires in nov 2013
    import pycurl, StringIO

    url = 'http://api.tinypng.org/api/shrink'
    key = 'api:Z1NUBU0JCIWQcDYoJnzeg33wrUnghzkJ'

    c = pycurl.Curl()
    c.setopt(pycurl.VERBOSE, 1)
    c.setopt(pycurl.URL, url)
    fout = StringIO.StringIO()
    c.setopt(pycurl.WRITEFUNCTION, fout.write)


    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.HTTPHEADER, [
        'Content-Type: image/png',
        key])
    filesize = os.path.getsize(path)
    c.setopt(pycurl.POSTFIELDSIZE, filesize)
    fin = open(path, 'rb')
    c.setopt(pycurl.READFUNCTION, fin.read)


    c.perform()
    response_code = c.getinfo(pycurl.RESPONSE_CODE)
    response_data = fout.getvalue()
    c.close()

    import json, urllib2

    if response_code == 200: # Success LOG(?)
        print response_data
        jData = json.loads(response_data)
        u = urllib2.urlopen(jData['output']['url'])

        localFile = open(path, 'wb')
        localFile.write(u.read())
        localFile.close()
    else: # Error LOG
        return

    return


def uniqueFile(path):
    """
    From path to file :
        returns new_Dir
        returns new_FileName
    """
    import re
    dir, fileName = os.path.split(path)
    fileName = re.sub('[^A-Za-z0-9_.-]', '', fileName)
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

def setPageBookID(sender, instance, **kwargs):
    instance.setPageBookID()

## Resize images after saving
post_save.connect(resizeImg, sender=Client)
post_save.connect(resizeImg, sender=PageBook)
post_save.connect(resizeImg, sender=PhotoMembre)
