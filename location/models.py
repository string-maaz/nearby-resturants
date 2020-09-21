# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

class LatLng(models.Model):
    lat = models.CharField(_('Latitude'), blank=False, null=False, max_length = 50, default = '')
    lng = models.CharField(_('Latitude'), blank=False, null=False, max_length = 50, default = '')
    is_active = models.BooleanField(default = True)#for not deleting just deactivating
    class Meta:
        abstract = True

class Resturant(models.Model):
    place_id = models.TextField(_('ID'), null=True, unique = True )
    resturant_name = models.CharField(_('Name'),db_index=True, blank=False, null=False, max_length = 150 )
    resturant_address = models.CharField(_('Name'),db_index=True, blank=False, null=False, max_length = 500 )
    comment_count = models.PositiveIntegerField(_("jersy_number"), default=0)

    class Meta:
        verbose_name = _("Resturants")
        verbose_name_plural = _("Resturants")

    def __unicode__(self):
        return str(self.resturant_name)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='st_comments',editable=False)
    resturant = models.ForeignKey(Resturant, related_name='resturant_comment')
    comment = models.TextField(_("comment"))
    

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __unicode__(self):
        try:
            return str(self.comment_html)
        except:
            return str(self.id)

