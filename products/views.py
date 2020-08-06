from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
# Create your views here.


class SearchProduct(ListView):
    model = Product
    template_name = 'products/search.html'

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Product.objects.filter(name__icontains=query)
        return object_list

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 10



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'



def category_product_list(request, slug):
    categories = Category.objects.all()
    product = Product.objects.all()

    category = get_object_or_404(Category, slug=slug)
    products = product.filter(category=category)

    # Pagination
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    product_page = paginator.get_page(page)


    context = {
        'category': category,
        'all_product': product,
        'categories': categories,
        'products': products,
        'product_page': product_page
        }

    return render(request,'category/categoties.html',context)
