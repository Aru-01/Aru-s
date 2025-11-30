from django.urls import path
from product import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="Product-list"),
    path("<int:id>/", views.ProductDetails.as_view(), name="Product-Details"),
]
