# Generated by Django 4.0.4 on 2022-10-21 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_purchasebill_amtrecvd_purchasebill_balance_due_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='creditperiod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newperiod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='paymentmethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newmethod', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='purchasepayment',
            fields=[
                ('pymntid', models.AutoField(primary_key=True, serialize=False, verbose_name='pyid')),
                ('reference', models.IntegerField(default=1000)),
                ('vendor', models.CharField(max_length=100)),
                ('paymentdate', models.DateField(null=True)),
                ('paymentmethod', models.CharField(max_length=100, null=True)),
                ('depositeto', models.CharField(max_length=100)),
                ('amtreceived', models.CharField(max_length=100, null=True)),
                ('paymentamount', models.CharField(max_length=100, null=True)),
                ('amtcredit', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='purchasepayment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billdate', models.DateField(null=True)),
                ('billno', models.CharField(max_length=100, null=True)),
                ('billamount', models.CharField(max_length=100, null=True)),
                ('amountdue', models.CharField(max_length=100, null=True)),
                ('payments', models.CharField(max_length=100, null=True)),
                ('pymnt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.purchasepayment')),
            ],
        ),
    ]
