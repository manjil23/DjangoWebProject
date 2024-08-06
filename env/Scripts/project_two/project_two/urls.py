from django.contrib import admin
from django.urls import path
from appone import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('productDetails/', views.userProfileDetails),
    path('conatinsProductName/', views.conatinsProductName),
    path('iconatinsProductName/', views.iconatinsProductName),
    path('greaterThanProductName/', views.greaterThanProductName),
    path('greaterThanEqualProductName/', views.greaterThanEqualProductName),
    path('productNameStartsWith/', views.productNameStartsWith),
    path('productNameEndsWith/', views.productNameEndsWith),
    path('productNameExact/', views.productNameExact),
    path('iproductNameExact/', views.iproductNameExact),
    path('userNameExclude/', views.userNameExclude),
    path('productNamesExcludeOr/', views.productNamesExcludeOr),
    path('productNamesExcludeAnd/', views.productNamesExcludeAnd),
    path('maxProductPrice/', views.maxProductPrice),
    path('minProductPrice/', views.minProductPrice),
    path('valuesMethod/', views.valuesMethod),
    path('values_listMethod/', views.values_listMethod),
    path('orderByCostDesc/', views.orderByCostDesc),
    path('orderByCostAscen/', views.orderByCostAscen),
    path('insertCreate/', views.insertCreate),
    path('insertBySave/', views.insertBySave),
    path('updateRecords/', views.updateRecords),
    path('bulkCreate/', views.bulkCreate),
    path('about/', views.about),
    path('contactus/', views.contactus),
    path('search_results/', views.search_results, name='search_results'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
