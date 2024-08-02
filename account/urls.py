from django.urls import path, include

from . import views as v


urlpatterns = [
    path('create/', v.UserCreateListView.as_view(), name='user_create_or_list'),
    path('detail/<int:id>/', v.UserDetailview.as_view(), name='detail'),

]
