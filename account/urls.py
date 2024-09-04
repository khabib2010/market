from django.urls import path, include

from . import views as v


urlpatterns = [
    path('create/', v.UserCreateListView.as_view(), name='user_create_or_list'),
    path('detail/<int:id>/', v.UserDetailview.as_view(), name='detail'),
    path('category_create',v.CategoryCreate.as_view(),name='create_category'),
    path('change/password',v.Change_password.as_view(),name='change_password'),
    path('create/product/',v.Productcreate.as_view(),name='productcreate'),
    path('product_detail/<int:id>',v.Product_detail_view.as_view(),name='product_detail'),
    path('category_detail/<int:id>',v.Category_detail_view.as_view(),name='category_detail'),
    path('savat/create/<int:id>',v.Savatcreate.as_view(),name='savat_create')
    


]
