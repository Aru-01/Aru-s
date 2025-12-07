from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from product.models import Product, Category, Review, ProductImage
from product.serializers import (
    ProductSerializer,
    CategorySerializer,
    ReviewSerializer,
    ProductImageSerialilzer,
)
from product.filters import ProductFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from product.permissions import IsReviewAuthorOrReadOnly


# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProductViewSet(ModelViewSet):
    """
    Product API ViewSet

    This ViewSet provides full CRUD operations for Product model.

    Features:
    - List all products with pagination
    - Retrieve single product by ID
    - Create new product (Admin only)
    - Update existing product (Admin only)
    - Delete product (Admin only)
    - Search by name and description
    - Filter products using custom filters
    - Order products by price and updated time
    """

    queryset = Product.objects.prefetch_related("images").all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ["name", "description"]
    ordering_fields = ["price", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(
        operation_summary="List all products",
        operation_description="""
        Retrieve a paginated list of all available products.

        ✅ Features:
        - Search by product name and description
        - Filter by category, price range, etc.
        - Order by price or last updated time

        ❌ Only admins can create/update/delete products.
        """,
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve single product",
        operation_description="Get detailed information of a single product using its ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create new product",
        operation_description="Create a new product. ✅ Only admins are allowed.",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update product",
        operation_description="Update existing product information. ✅ Only admins are allowed.",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete product",
        operation_description="Delete a product from the system. ✅ Only admins are allowed.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ProductImageViewSet(ModelViewSet):
    """
    Product Image API ViewSet

    This ViewSet manages image uploads and retrieval for individual products.

    Features:
    - List all images of a specific product
    - Upload new images for a product (Admin only)
    - Update product images (Admin only)
    - Delete product images (Admin only)
    """

    serializer_class = ProductImageSerialilzer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs["product_pk"])

    def perform_create(self, serializer):
        return serializer.save(product_id=self.kwargs["product_pk"])
    
    @swagger_auto_schema(
        operation_summary="List product images",
        operation_description="Retrieve all images for a specific product using product ID."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Upload product image",
        operation_description="Upload a new image for a product. ✅ Only admins are allowed."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update product image",
        operation_description="Update an existing product image. ✅ Only admins are allowed."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete product image",
        operation_description="Delete a product image permanently. ✅ Only admins are allowed."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count("products")).all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminOrReadOnly]


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs["product_pk"])

    def get_serializer_context(self):
        return {"product_id": self.kwargs["product_pk"]}
