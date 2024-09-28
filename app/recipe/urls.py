"""
URL mapping for recipe app API
"""

from django.urls import include, path
from recipe import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipe', views.RecipeViewsets)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]