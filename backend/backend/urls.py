from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('administration.urls')),
    path('api/v1/inventory/', include('inventory.urls'))

]
