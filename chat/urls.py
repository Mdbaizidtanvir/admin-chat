from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.homepage, name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path("<int:pk>/", views.chatroom, name="chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),

path('offer/', views.offer, name='offer'),
path('answer/', views.answer, name='answer'),
path('ice_candidate/', views.ice_candidate, name='ice_candidate'),

path('sfsd', views.message_File_upload, name="file-upload")
]
