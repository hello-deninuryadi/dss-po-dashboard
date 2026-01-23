from django.urls import path
from .views import DecisionOverrideCreateView
from .views import ItemDSSListView
from .views import DecisionOverrideListView

urlpatterns = [
    path('items/', ItemDSSListView.as_view(), name='item-dss-list'),
    path('override/', DecisionOverrideCreateView.as_view()),
    path("override/history", DecisionOverrideListView.as_view()),
    path("override/history/<str:item_code>/", DecisionOverrideListView.as_view()),
    ]