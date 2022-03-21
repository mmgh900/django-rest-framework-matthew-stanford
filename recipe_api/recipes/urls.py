from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.RecipeListView.as_view()),
    path('create/', views.RecipeCreateView.as_view()),
    path('<int:pk>/upvote/', views.UpVoteCreateView.as_view()),
    path('<int:pk>/', views.RecipeDetailedView.as_view()),
    path('<int:pk>/update', views.RecipeUpdateView.as_view()),

]
ingredientUrls = [
    path('', views.IngredientListView.as_view()),
    path('create/', views.IngredientCreateView.as_view()),
]
