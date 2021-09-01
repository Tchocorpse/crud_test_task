import hashlib

from django.db import models


class Image(models.Model):
    id = models.AutoField(primary_key=True)

    image = models.ImageField(upload_to='images_storage')
    image_size = models.IntegerField(blank=False, null=False)
    hash_value = models.CharField(max_length=32, blank=False, null=False)

    def file_hash(self):
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: self.image.file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def file_size(self):
        return self.image.size

    def save(self, *args, **kwargs):
        self.hash_value = self.file_hash()
        self.image_size = self.file_size()
        super(Image, self).save(*args, **kwargs)


class Commentary(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    text = models.TextField()
    hash_value = models.CharField(max_length=32, blank=False, null=False)

    def text_hash(self, text):
        return hashlib.md5(text.encode()).hexdigest()

    def save(self, *args, **kwargs):
        self.hash_value = self.text_hash(self.text)
        super(Commentary, self).save(*args, **kwargs)
