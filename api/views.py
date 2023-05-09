from rest_framework.views import APIView
from .models import Category, Dish, Review
from .serializers import CategorySerializer, RecipeSerializer, ReviewSerializer
from rest_framework.response import Response


class CategoryView(APIView):
    def get(self, request):
        output = [
            {
                'name': output.name,
                'detail': output.detail,
            } for output in Category.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    
class RecipeView(APIView):
    def get(self, request):
        output = [
            {
                'category': output.category,
                'name': output.name,
                'calorie': output.calorie,
                'ingredients': output.ingredients,
                'steps': output.steps,
                'image': output.image,
            } for output in Dish.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ReviewView(APIView):
    def get(self, request):
        output = [
            {
                'email': output.email,
                'name': output.name,
                'detail': output.detail,
            } for output in Review.objects.all()
        ]
        return Response(output)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# У каждого блюда и каждой категории должна быть своя страница: с главной страницы можно перейти на любую из категорий, 
# а из категории — на любой рецепт этой категории.


# class CategoryDetailView(viewsets.ModelViewSet):        
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class RecipeDetailView(viewsets.ModelViewSet):
#     queryset = Dish.objects.all()
#     serializer_class = RecipeSerializer

#     def get_queryset(self):
#         recipes = Dish.objects.filter(category=self.kwargs['pk'])
#         return recipes
    