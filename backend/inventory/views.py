from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import Sale
from .serializers import SalesSerializer

from django.http import JsonResponse


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):

        return JsonResponse({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'data': data,
        })


class ResponseFormatter:
    @staticmethod
    def formatter(**data):
        return JsonResponse(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getSales(request):
    try:
        sales = Sale.objects.using('sale').values('material_code', 'billing_date', 'customer_code', 'sales',
                                                  'margins').order_by('billing_date')

        if sales:
            if request.method == 'GET' and 'page_size' and 'page' in request.GET:
                page_size = int(request.GET.get('page_size'))
                page = int(request.GET.get('page'))
                paginator = CustomPagination()
                paginator.page_size = page_size
                paginator.page = page

                result_page = paginator.paginate_queryset(sales, request)
                sales_serializer = SalesSerializer(result_page, many=True)
                return paginator.get_paginated_response(sales_serializer.data)
            elif request.method == 'GET' and 'page_size' in request.GET:
                page_size = int(request.GET.get('page_size'))
                paginator = CustomPagination()
                paginator.page_size = page_size

                result_page = paginator.paginate_queryset(sales, request)
                sales_serializer = SalesSerializer(result_page, many=True)
                return paginator.get_paginated_response(sales_serializer.data)
            elif request.method == 'GET':
                sales_serializer = SalesSerializer(sales, many=True)
                return ResponseFormatter.formatter(data=sales_serializer.data)
        else:
            return ResponseFormatter.formatter(data=[])

    except Exception as e:
        return ResponseFormatter.formatter(data=str(e))
