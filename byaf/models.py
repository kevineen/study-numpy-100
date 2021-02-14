import shutil
from django.db import models


# Create your models here.
class PDFPack(models.Model):

    template = "program/pdfpack.html"

    upload = models.FileField(upload_to="pdfbatch/%Y%m%d%H%M/", verbose_name="加工ファイル")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "PDFPack"
        verbose_name_plural = "PDFPacks"

    def __str__(self):
        return str(self.pk)
