from django.urls import path
from .views import recipe_create_list, recipe_retrieve_update_delete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('recipes/', recipe_create_list, name='recipe-create-list'),
    path('recipes/<int:pk>/', recipe_retrieve_update_delete, name='recipe-rud'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]