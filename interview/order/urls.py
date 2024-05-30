
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListBetweenStartAndEndDateView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('embargo_date/', OrderListBetweenStartAndEndDateView.as_view(), name='order-embargo-date'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]