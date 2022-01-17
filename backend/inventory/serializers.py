from rest_framework import serializers

from .models import Sale


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['material_code', 'billing_date', 'customer_code', 'sales', 'margins']