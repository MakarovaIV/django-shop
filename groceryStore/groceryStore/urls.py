"""groceryStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from grocery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.CategoryListView.as_view(), name="category"),
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('login/', views.login_handler, name='login'),
    path('logout/', views.logout_handler, name='logout'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('category/<int:category_id>/', views.ProductListView.as_view(), name='category_detail'),    # Product list
    path('category/<int:category_id>/product/<int:product_id>/', views.ProductListView.as_view(),
         name='product_detail'),
    path('category/<int:category_id>/product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('category/<int:category_id>/product/update/<int:pk>/', views.ProductUpdateView.as_view(),
         name='product_update'),
    path('category/<int:category_id>/product/delete/<int:pk>/', views.ProductDeleteView.as_view(),
         name='product_delete'),

    path('cart/', views.cart_view, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    # path('order/', views.make_order, name='make_order'),
    path('order/', views.MakeOrderView.as_view(), name='make_order'),
    path('cart/order/submit/', views.OrderPaymentView.as_view(), name='submit_order'),

    path('cart/order/list/', views.OrderListView.as_view(), name='order_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
