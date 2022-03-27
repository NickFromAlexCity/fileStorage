from django.db import models
from .utils import make_thumbnail


class File(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    preview = models.ImageField(upload_to='previews/', null=True, blank=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        #self.preview.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # save for image
        super(File, self).save(*args, **kwargs)
        try:
            make_thumbnail(self.preview, self.file, (50, 50), '_preview')
            # save for thumbnail and icon
            super(File, self).save(*args, **kwargs)
        except:
            pass