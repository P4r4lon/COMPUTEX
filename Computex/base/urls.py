
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='home'),
    #stands
    path('stands', views.stands, name='stands'),
    path('stands/<int:pk>', views.standsDetailView.as_view(), name='stands_view'),

    path('suppliers', views.suppliers, name='suppliers'),
    path('suppliers_create', views.suppliers_create, name ='suppliers_create'),
    path('suppliers_delete/<int:pk>', views.suppliers_delete, name ='suppliers_delete'),
    path('suppliers_update/<int:pk>', views.suppliers_update.as_view(), name = 'suppliers_update'),

    path('media', views.media, name='media'),
    path('media_create', views.media_create, name='media_create'),
    path('media_delete/<int:pk>', views.media_delete, name = 'media_delete'),
    path('media_update/<int:pk>', views.media_update.as_view(), name = 'media_update'),

    path('stands/<int:pk>/application_create', views.application_create, name='app_create'),
    path('applications/<slug:filter>', login_required(views.applications), name='applications'),
]
