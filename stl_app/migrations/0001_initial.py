# Generated by Django 4.1.1 on 2022-10-25 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('sub_category_name', models.CharField(max_length=50)),
                ('category_image', models.ImageField(upload_to='./static/image')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Model_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('who_aploaded', models.CharField(max_length=50)),
                ('short_discription', models.CharField(max_length=100)),
                ('stl_model_image', models.ImageField(upload_to='./static/image')),
                ('stl_file', models.FileField(upload_to='./static/stl')),
                ('model_discription', models.TextField(max_length=2000)),
                ('model_tag', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stl_app.model_category')),
            ],
        ),
    ]