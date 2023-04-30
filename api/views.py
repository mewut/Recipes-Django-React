from rest_framework import viewsets
from .models import Category, Dish, Review
from .serializers import CategorySerializer, RecipeSerializer, ReviewSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class RecipeView(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = RecipeSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

# У каждого блюда и каждой категории должна быть своя страница: с главной страницы можно перейти на любую из категорий, 
# а из категории — на любой рецепт этой категории.


class CategoryDetailView(viewsets.ModelViewSet):        
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeDetailView(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        recipes = Dish.objects.filter(category=self.kwargs['pk'])
        return recipes
    