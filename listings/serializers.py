from rest_framework import serializers
from listings.models import Listing, HotelRoom, HotelRoomType, BookingInfo


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_type', 'title', 'country', 'city', 'price']
