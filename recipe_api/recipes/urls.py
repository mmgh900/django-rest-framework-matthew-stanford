from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.ListCreateRecipes.as_view()),
    path('<int:pk>/upvote/', views.CreateUpvote.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyRecipe.as_view()),

]
ingredientUrls = [
    path('', views.ListCreateRecipes.as_view()),
]
