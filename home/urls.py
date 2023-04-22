from home.views import tester

urlpatterns = [
    path('', views.index, name='index'),
    path('tester/', views.tester, name='tester'),
]