# Generated by Django 3.2 on 2021-04-27 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_type', models.CharField(choices=[('hotel', 'Hotel'), ('apartment', 'Apartment')], default='apartment', max_length=16)),
                ('title', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room_types', to='listings.listing')),
            ],
        ),
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=255)),
                ('hotel_room_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_rooms', to='listings.hotelroomtype')),
            ],
        ),
        migrations.CreateModel(
            name='BookingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hotel_room_type', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_info', to='listings.hotelroomtype')),
                ('listing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_info', to='listings.listing')),
            ],
        ),
    ]
