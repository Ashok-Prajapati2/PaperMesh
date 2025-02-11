from django.shortcuts import render
from homeapp.models import Category, Fashion
from django.core.paginator import Paginator
from django.views import View

global_data = None

def paginator_function(data, show, request):
    paginator = Paginator(data, show)
    page_num = request.GET.get('page')
    f_data = paginator.get_page(page_num)
    total_page = f_data.paginator.num_pages
    return {'f_data': f_data, 'total_page': total_page}

class HomePageView(View):
    template_name = 'homepage.html'
    items_per_page = 3

    def get(self, request):
        category_items = Category.objects.all().order_by('category_name')
        fashion_data_n = Fashion.objects.all().order_by('item_name')
        fashion_data = paginator_function(fashion_data_n, self.items_per_page, request)
        
        context = {
            'fashion_data': fashion_data['f_data'],
            'total_page': fashion_data['total_page'],
            'category_items': category_items,
        }
        return render(request, self.template_name, context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about-us.html')

def category(request):
    category_items = Category.objects.all().order_by('category_name')
    fashion_data = Fashion.objects.all().order_by('item_name')
    
    context = {
        'fashion_data': fashion_data,
        'category_items': category_items,
    }
    return render(request, 'category.html', context)