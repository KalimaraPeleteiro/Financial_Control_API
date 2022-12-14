"""FinancialControlAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from RevenueExpenseControl.views import *
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Financial Control API",
      default_version='v1',
      description="An API for Financial Control",
      terms_of_service="#",
      contact=openapi.Contact(email="kalimarapeleteiro@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='Receitas')
router.register('despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include(router.urls)),
    path('receitas/<int:pk>/', ReceitaEspecificaViewSet.as_view()),
    path('despesas/<int:pk>/', DespesaEspecificaViewSet.as_view()),
    path('receitas/<int:year>/<int:month>/', ReceitaMesViewSet.as_view()),
    path('despesas/<int:year>/<int:month>/', DespesaMesViewSet.as_view()),
    path('resumo/<int:year>/<int:month>/', ResumoViewSet.as_view()),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-swagger-ui')
]
