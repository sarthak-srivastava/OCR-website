# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_auto_20170815_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='/pic_folder/'),
        ),
    ]
