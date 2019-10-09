from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    # path('', views.about, name='about'),
]
