from django.urls import path
from .views import OrganizationListAPIView, OrganizationDetailAPIView

urlpatterns = [
    # Get all organizations (requires token authentication)
    path('organizations/', OrganizationListAPIView.as_view(), name='organization-list'),

    # Get details of a single organization (requires token authentication)
    path('organizations/<int:pk>/', OrganizationDetailAPIView.as_view(), name='organization-detail'),
]
