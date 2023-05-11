from django.urls import path
from . import views
from items.views import ItemListCreateAPIView


urlpatterns = [
    path('', views.StoresAPIView.as_view(), name = 'stores'),
    path('<int:id>', views.StoreDetailAPIView.as_view(), name = 'store'),
    path('<int:store_id>/items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    
]
