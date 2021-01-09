from django.urls import path
from .views import HomePageView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('sample/', SamplePageView.as_view(), name="sample"),
]