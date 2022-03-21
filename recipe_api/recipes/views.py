from urllib import request
from rest_framework import generics, permissions

from .models import Ingredient, Recipe, UpVote
from .serializers import IngredientSerializer, RecipeDetailSerializer, RecipeSerializer, UpVoteSerializer
from rest_framework import exceptions


class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if (self.request.user.is_authenticated):
            serializer.save(author=self.request.user)
        else:
            raise exceptions.PermissionDenied


class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permissions_classes = [permissions.AllowAny]


class IngredientListView(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    premission_class = [permissions.AllowAny]


class IngredientCreateView(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    premission_class = [permissions.IsAuthenticated]


class UpVoteCreateView(generics.CreateAPIView):
    serializer_class = UpVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

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


class RecipeDetailedView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    permission_classes = [permissions.AllowAny]


class RecipeUpdateView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        recipe = Recipe.objects.filter(
            author=self.request.user, pk=kwargs['pk'])
        if recipe.exists:
            return self.destroy(request, *args, **kwargs)
        else:
            raise exceptions.ValidationError(
                "This is not your recipe, so you can't delete it!")
