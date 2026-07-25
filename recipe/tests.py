from django.test import TestCase
from recipe.models import Recipe
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.
class RecipeModelTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            title="CHICKEN INN RECIPE",
            description='classsic kfc chicken clone',
            ingredients="Chicken, cooking oil, spices, baking flour",
            instructions="1. boil the chicken, 2. marinate the chicken, 3.fry the chicken"
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "CHICKEN INN RECIPE")
        self.assertEqual(self.recipe.description, "classsic kfc chicken clone")
        self.assertEqual(self.recipe.ingredients, "Chicken, cooking oil, spices, baking flour")
        self.assertEqual(self.recipe.instructions, "1. boil the chicken, 2. marinate the chicken, 3.fry the chicken")

class RecipeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="chalie", password="@Password101")
        self.client.force_authenticate(user=self.user)
        self.recipe = Recipe.objects.create(
            title="CHICKEN INN RECIPE",
            description='classsic kfc chicken clone',
            ingredients="Chicken, cooking oil, spices, baking flour",
            instructions="1. boil the chicken, 2. marinate the chicken, 3.fry the chicken"
        )

        self.valid_payload = {
            "title":"CHICKEN INN RECIPE",
            "description":'classsic kfc chicken clone',
            "ingredients":"Chicken, cooking oil, spices, baking flour",
            "instructions":"1. boil the chicken, 2. marinate the chicken, 3.fry the chicken"
        }

        self.invalid_payload = {
            "name":"KFC",
            "description":'classsic kfc chicken clone',
            "ingredients":"Chicken, cooking oil, spices, baking flour",
            "instructions":"1. boil the chicken, 2. marinate the chicken, 3.fry the chicken"
        }

    def test_get_all_recipes(self):
        response = self.client.get('/api/v1/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      
    def test_create_valid_recipe(self):
        response = self.client.post('/api/v1/recipes/', self.valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_recipe(self):
        response = self.client.post('/api/v1/recipes/', self.invalid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_recipes_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/recipes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

