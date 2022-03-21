from rest_framework import generics, permissions

from recipe_api.authentication import BearerAuthentication

from .models import Ingredient, Recipe, UpVote
from .serializers import IngredientSerializer, RecipeDetailSerializer, RecipeSerializer, UpVoteSerializer
from rest_framework import exceptions
from rest_framework.response import Response

class ListCreateRecipes(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RetrieveUpdateDestroyRecipe (generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = RecipeDetailSerializer(queryset, many=True)
        return Response(serializer.data)
            
    def delete(self, request, *args, **kwargs):
        recipe = Recipe.objects.filter(
            author=request.user, pk=kwargs['pk'])
        if recipe.exists:
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.PermissionDenied(
                "This is not your recipe, so you can't delete it!")

class ListCreateIngredients(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class CreateUpvote(generics.CreateAPIView):
    serializer_class = UpVoteSerializer

    def get_queryset(self):
        user = self.request.user
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return UpVote.objects.filter(user=user, recipe=recipe)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise exceptions.ValidationError("You have already voted on this!")
        user = self.request.user
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=user, recipe=recipe)

