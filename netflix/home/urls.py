from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name="add"),
    path('movie/<int:movie_id>/', views.edit_movies, name="edit-movies"),
    path('delete/<int:movie_id>/', views.delete, name="delete"),
    path('update/<int:movie_id>/', views.update, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
