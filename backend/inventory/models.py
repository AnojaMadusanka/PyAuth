from django.db import models


class Sale(models.Model):
    material_code = models.TextField(db_column='MaterialCode', null=False, blank=False)
    billing_date = models.TextField(db_column='BillingDate', null=False, blank=False)
    customer_code = models.TextField(db_column='CustomerCode', null=False, blank=False)
    sales = models.FloatField(db_column='Sales', null=False, blank=False)
    margins = models.FloatField(db_column='Margins', null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'sale'

    def __str__(self):
        return self.material_code
