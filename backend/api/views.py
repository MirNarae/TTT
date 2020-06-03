from api import models, serializers
from rest_framework import viewsets
from rest_framework.response import Response

from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination
import pandas as pd
import numpy as np
from django.http import JsonResponse


class SmallPagination(PageNumberPagination):
    page_size = 5000
    page_size_query_param = "page_size"
    max_page_size = 5000

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StockSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        code = self.request.query_params.get("code", "A000020")
        month = self.request.query_params.get("month", 0)
        queryset = models.Stock.objects.all().order_by("date")
        if code is not "":
            queryset = queryset.filter(code = code)
            
        return queryset

class StockInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StockInfoSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        queryset = models.StockInfo.objects.all()
        return queryset


