from django.shortcuts import render
from .models import Category, Fashion
from django.core.paginator import Paginator

# Function to handle pagination logic
def paginator_function(data, show, request):
    """
    Helper function to paginate data
    Args:
        data: QuerySet to paginate
        show: Number of items per page
        request: HttpRequest object
    Returns:
        Dictionary with paginated data and total pages
    """
    paginator = Paginator(data, show)
    page_num = request.GET.get('page')
    f_data = paginator.get_page(page_num)
    total_page = f_data.paginator.num_pages
    return {'f_data': f_data, 'total_page': total_page}

# Homepage view to display fashion items with pagination
def homepage(request):
    """
    View function for the homepage
    Displays fashion items with pagination and categories
    """
    category_items = Category.objects.all().order_by('category_name')
    fashion_data_n = Fashion.objects.all().order_by('item_name')
    fashion_data = paginator_function(fashion_data_n, 3, request)
    total_page = fashion_data['total_page']
    fashion_data = fashion_data['f_data']
    
    data = {
        'fashion_data': fashion_data,
        'total_page': total_page,
        'category_items': category_items,
    }

    return render(request, 'homepage.html', data)
