from django.urls import path
from . import views
from backend.apps.tintuc.views import(
    TinTucView,
    TinTucDetailView
)

urlpatterns = [
    path('', TinTucView.as_view(),name='TinTucView'),
    #path('tintuc/', TinTucView.as_view()),
    #path('tintuc/([0-9]+)/', TinTucDetailView.as_view())
    path('([0-9]+)/', TinTucDetailView.as_view())
]
