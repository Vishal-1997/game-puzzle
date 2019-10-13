from django.urls import path

from list import views
from list.views import game_view_id_filter, game_view_title_filter

urlpatterns = [
    path('all/', views.game_view),
    path('row/<int:id>/', game_view_id_filter),
    path('row/<int:id>/', game_view_title_filter),
]
