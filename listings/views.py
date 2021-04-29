import django_filters.rest_framework
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from listings.serializers import ListingSerializer
from listings.models import Listing, HotelRoom, HotelRoomType, BookingInfo
from rest_framework import generics, filters
from booking_engine.settings import *
from django_filters.rest_framework import DjangoFilterBackend


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Listing.objects.all().order_by('price')
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['listing_type', 'title', 'country', 'city', 'price']
    search_fields =  ['listing_type', 'title', 'country', 'city', 'price']


class ListingFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="price", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="price", lookup_type='lte')

    class Meta:
        model = Listing
        fields = ['min_price', 'max_price']

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_class = ListingFilter
