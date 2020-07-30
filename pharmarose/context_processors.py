from products.models import Category, Product

def all_categories(request):
    all_categories = Category.objects.all().select_related('parent').prefetch_related('categories')
    return {'all_categories': all_categories}

def all_products(request):
    all_products = Product.objects.all().select_related('category')
    return {'all_products': all_products}
