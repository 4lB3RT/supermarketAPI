from django.urls import path, include

from app.Category.Infrastructure.Controller.GetCategoriesController import GetCategoriesController

urlpatterns = [
    path('categories/', GetCategoriesController.as_view(), name="get"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]   