from django.db import models


class COadbms(models.Model):
    co_no = models.CharField(max_length=2)
    description = models.CharField(max_length=500)
    po1 = models.CharField(max_length=1)
    po2 = models.CharField(max_length=1)
    po3 = models.CharField(max_length=1)
    po4 = models.CharField(max_length=1)
    po5 = models.CharField(max_length=1)
    po6 = models.CharField(max_length=1)

    def __str__(self):
        return 'CO' + self.co_no


class PO(models.Model):
    po_no = models.CharField(max_length=2)
    description = models.CharField(max_length=500)

    def __str__(self):
        return 'PO' + self.po_no


class COatdadbms(models.Model):
    cono = models.CharField(max_length=2)
    atd = models.CharField(max_length=50)

    def __str__(self):
        return self.cono + ' - ' + self.atd