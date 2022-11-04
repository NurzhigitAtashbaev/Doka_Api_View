from django.urls import path

from . import views


urlpatterns = [
    path('news-create/', views.news_create),
    path('news-detail/<int:pk>/', views.NewsRetrieveAPIView.as_view()),
    path('news-list/', views.NewsListAPIView.as_view()),
    path('news-delete/<int:pk>/', views.NewsDeleteAPIView.as_view()),

]