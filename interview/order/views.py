from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer, \
    OrderListBetweenStartAndEndDateViewInputSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListBetweenStartAndEndDateView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Filter the orders returned to only ones with embargo_date between provided dates
        """
        serializer = OrderListBetweenStartAndEndDateViewInputSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        return self.queryset.filter(embargo_date__range=[serializer.validated_data["start_date"], serializer.validated_data["end_date"]])
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
