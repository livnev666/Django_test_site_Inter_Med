from django.urls import path
from test_datatable import views as views_med
from django.views.decorators.cache import cache_page

urlpatterns = [

    path('', cache_page(60)(views_med.ListViewStudies.as_view()), name='init_db'),
    path('one_patient/<int:pk>/', views_med.DetailPatient.as_view(), name='detail'),

]