from dataclasses import field
import re
from rest_framework import serializers
from .models import Ingredient, Recipe, UpVote
from django.db.models import Sum


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'calories')
        read_only_fields = tuple('id')


class RecipeSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField()
    total_calories = serializers.SerializerMethodField()

    def get_upvotes(self, recipe):
        return UpVote.objects.filter(recipe=recipe).count()

    def get_total_calories(self, recipe):
        return Ingredient.objects.filter(recipe=recipe).aggregate(Sum('calories'))

    class Meta:
        model = Recipe
        fields = ('id', 'author', 'title', 'image', 'time_mins',
                  'ingredients', 'diet', 'total_calories',  'created', 'updated', 'upvotes')
        read_only_fields = ('id', 'author')


class UpVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = ('id',)
        read_only_fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
