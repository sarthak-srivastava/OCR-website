from django.db import models

class Images(models.Model):
	image= models.ImageField(upload_to = '/pic_folder/', default = 'pic_folder/None/no-img.jpg')
	
