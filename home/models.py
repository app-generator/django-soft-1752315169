# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nama_depan = models.CharField(max_length=255, null=True, blank=True)
    nama_belakang = models.CharField(max_length=255, null=True, blank=True)
    nomor_hp = models.IntegerField(null=True, blank=True)
    dapukan = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Daerah(models.Model):

    #__Daerah_FIELDS__
    id_daerah = models.IntegerField(null=True, blank=True)
    nama_daerah = models.CharField(max_length=255, null=True, blank=True)

    #__Daerah_FIELDS__END

    class Meta:
        verbose_name        = _("Daerah")
        verbose_name_plural = _("Daerah")


class Desa(models.Model):

    #__Desa_FIELDS__
    id_desa = models.IntegerField(null=True, blank=True)
    nama_desa = models.CharField(max_length=255, null=True, blank=True)
    id_daerah = models.ForeignKey(Daerah, on_delete=models.CASCADE)

    #__Desa_FIELDS__END

    class Meta:
        verbose_name        = _("Desa")
        verbose_name_plural = _("Desa")


class Kelompok(models.Model):

    #__Kelompok_FIELDS__
    id_kel = models.IntegerField(null=True, blank=True)
    nama_kel = models.CharField(max_length=255, null=True, blank=True)
    id_desa = models.ForeignKey(Desa, on_delete=models.CASCADE)

    #__Kelompok_FIELDS__END

    class Meta:
        verbose_name        = _("Kelompok")
        verbose_name_plural = _("Kelompok")


class Data_Master(models.Model):

    #__Data_Master_FIELDS__
    id_data = models.IntegerField(null=True, blank=True)
    nama = models.CharField(max_length=255, null=True, blank=True)
    nomor_hp = models.IntegerField(null=True, blank=True)
    id_daerah = models.ForeignKey(Daerah, on_delete=models.CASCADE)
    id_desa = models.ForeignKey(Desa, on_delete=models.CASCADE)
    id_kel = models.ForeignKey(Kelompok, on_delete=models.CASCADE)
    create_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Data_Master_FIELDS__END

    class Meta:
        verbose_name        = _("Data_Master")
        verbose_name_plural = _("Data_Master")



#__MODELS__END
