
from django.urls import path
from .views import BillCreateAPIView, BillListByStoreId, BillDetailAPIView, BillProductListView, PayBillView, StoreBillProfitView, UpdateBillView, DeleteBillView

urlpatterns = [
    path('createBill/', BillCreateAPIView.as_view(),
         name='create_bill_into_redis_api'),
    path('bills/by-store/', BillListByStoreId.as_view(), name='bill-list-by-store'),
    path('bill-detail/<str:key>/', BillDetailAPIView.as_view(), name='bill-detail'),
    path('update_bill/', UpdateBillView.as_view(), name='update_bill'),
    path('delete_bill/<str:bill_id>/',
         DeleteBillView.as_view(), name='delete_bill'),
    path('pay_bill/', PayBillView.as_view(), name='pay_bill'),
    path('store-bill-profit/<int:store_id>/',
         StoreBillProfitView.as_view(), name='store-bill-profit'),
    path('bills/<str:bill_id>/products/',
         BillProductListView.as_view(), name='bill-products-list'),
]
