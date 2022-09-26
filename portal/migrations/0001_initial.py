# Generated by Django 4.1.1 on 2022-09-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BECE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payeremail', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Payerphone', models.CharField(blank=True, max_length=100, null=True)),
                ('SchoolId', models.CharField(blank=True, max_length=100, null=True)),
                ('SchoolTypeId', models.CharField(blank=True, max_length=100, null=True)),
                ('RequestId', models.CharField(blank=True, max_length=100, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('PayerName', models.CharField(blank=True, max_length=100, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('NumberOfCandidates', models.IntegerField(blank=True, null=True)),
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
                ('TownCity', models.CharField(blank=True, max_length=100, null=True)),
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
        migrations.CreateModel(
            name='Portals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('LedNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('LedDistrict', models.CharField(blank=True, max_length=100, null=True)),
                ('RequestId', models.CharField(blank=True, max_length=100, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('StudentNumber', models.IntegerField(blank=True, null=True)),
                ('SchoolName', models.CharField(blank=True, max_length=200, null=True)),
                ('session_token', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ExamType', models.CharField(blank=True, choices=[('0', 'B.E.C.E'), ('1', 'JUNIOR SCHOOL'), ('2', 'M.C'), ('3', 'P.S')], default=0, max_length=100, null=True)),
                ('CandidateName', models.CharField(blank=True, max_length=100, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('AddressNo', models.CharField(blank=True, max_length=100, null=True)),
                ('Street', models.CharField(blank=True, max_length=100, null=True)),
                ('TownCity', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('testType', models.CharField(blank=True, choices=[('0', 'demola'), ('1', 'balogun'), ('2', 'surajudeen')], default=0, max_length=100, null=True)),
                ('combine', models.CharField(blank=True, choices=[('0', 'red'), ('1', 'yellow'), ('2', 'green')], default=0, max_length=100, null=True)),
                ('currentOffice', models.CharField(blank=True, max_length=100, null=True)),
                ('Mda', models.CharField(blank=True, max_length=100, null=True)),
                ('staffID', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('pinum', models.CharField(blank=True, max_length=100, null=True)),
                ('trnsref', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
