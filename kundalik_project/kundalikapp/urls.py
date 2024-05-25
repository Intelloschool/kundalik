from kundalik_project.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index')
]