from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [path('display',views.index, name = 'index'),
              path('entry',views.entry,name = 'entry'),]