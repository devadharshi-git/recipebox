from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm
from reviews.forms import ReviewForm

@login_required
def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    reviews = recipe.reviews.all()
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.recipe = recipe
        review.user = request.user
        review.save()
        return redirect('recipe_detail', pk=pk)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'reviews': reviews,
        'form': form
    })

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')
