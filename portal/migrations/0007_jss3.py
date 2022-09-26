# Generated by Django 3.2.3 on 2022-09-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20220925_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSS3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payeremail', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Payerphone', models.CharField(blank=True, max_length=100, null=True)),
                ('SchoolId', models.CharField(blank=True, max_length=100, null=True)),
                ('SchoolTypeId', models.CharField(blank=True, max_length=100, null=True)),
                ('schoolIds', models.CharField(blank=True, max_length=100, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('PayerName', models.CharField(blank=True, max_length=100, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('NumberOfCandidates', models.IntegerField(blank=True, default=0, null=True)),
                ('SchoolName', models.CharField(blank=True, max_length=200, null=True)),
                ('session_token', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('StartingDate', models.DateField(blank=True, null=True)),
                ('ClosingDate', models.DateField(blank=True, null=True)),
                ('ExamName', models.CharField(blank=True, max_length=100, null=True)),
                ('LgaId', models.CharField(blank=True, max_length=500, null=True)),
                ('LgaName', models.CharField(blank=True, max_length=500, null=True)),
                ('ExamCost', models.CharField(blank=True, max_length=500, null=True)),
                ('SchoolType', models.CharField(blank=True, choices=[('0', 'PRIVATE'), ('1', 'PUBLIC')], max_length=100, null=True)),
                ('Street', models.CharField(blank=True, max_length=100, null=True)),
                ('adminemail', models.CharField(blank=True, max_length=500, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('currentOffice', models.CharField(blank=True, max_length=100, null=True)),
                ('Mda', models.CharField(blank=True, max_length=100, null=True)),
                ('pinum', models.CharField(blank=True, max_length=500, null=True)),
                ('trnsref', models.CharField(blank=True, max_length=100, null=True)),
                ('uniquecode', models.CharField(blank=True, max_length=100, null=True)),
                ('quota', models.CharField(blank=True, max_length=100, null=True)),
                ('quota2', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]