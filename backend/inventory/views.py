from django.http import JsonResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import Sale
from .serializers import SalesSerializer

from django.http import JsonResponse


class ResponseFormatter:

    @staticmethod
    def formatter(**data):
        return JsonResponse(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getSales(request):
    try:
        page_size = int(request.GET.get('page_size'))
        page = int(request.GET.get('page'))

        paginator = PageNumberPagination()
        paginator.page_size = page_size
        paginator.page = page
        sales = Sale.objects.using('sale').values('material_code', 'billing_date', 'customer_code', 'sales',
                                                  'margins').order_by('billing_date')

        if sales:
            result_page = paginator.paginate_queryset(sales, request)
            sales_serializer = SalesSerializer(result_page, many=True)
            return ResponseFormatter.formatter(detail=sales_serializer.data, status=status.HTTP_200_OK, safe=False)
        else:
            return ResponseFormatter.formatter(detail="Data not found", status=status.HTTP_200_OK, safe=False)

    except Exception as e:
        return ResponseFormatter.formatter(detail=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)
