from django.urls import path

from . import views
app_name='bankapp'

urlpatterns = [
    path('', views.allBranches, name='allBranches'),
    path('<slug:c_slug>/', views.allBranches, name='branches_by_places'),
    # path('<slug:c_slug>/<slug:place_slug>/', views.placedetail, name='placecatdetail'),

]