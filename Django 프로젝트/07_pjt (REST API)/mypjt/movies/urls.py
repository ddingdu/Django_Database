from django.urls import path
from . import views

app_name ='movies'
urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('actors/', views.actor_list),
    path('actors/<int:actor_id>/', views.actor_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:review_id>/', views.review_detail),
    path('movies/<int:pk>/reviews/', views.create_review),
]
