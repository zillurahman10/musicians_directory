from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_musician, name = "add_musician"),
    # path('album/', include('album.urls'))
]
