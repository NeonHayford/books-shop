from django.urls import path
from .views import index, PublishBookView

urlpatterns = [
    path('', index, name='parent-contrib'),
    path('uploads', PublishBookView, name='publish_book')
]