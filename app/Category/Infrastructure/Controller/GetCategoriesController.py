from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt

from app.Category.Application.GetCategories.GetCategories import GetCategories
from app.Category.Infrastructure.Repository.ScrapyCategoryRepository import ScrapyCategoryRepository

class GetCategoriesController(APIView):    
    def __init__(self, *args, **kwargs) -> None:
        pass
            
    @csrf_exempt
    def get(self, request: Request, *args, **kwargs) -> Response:
        
        return  Response(status=200, data="test")


         