from django.shortcuts import render, get_object_or_404
from homeapp.models import Fashion

def product_details(request, product_id):
    product = get_object_or_404(Fashion, product_id=product_id)
    context = {
        'product': product,
        'product_image': product.item_img,
        'product_name': product.item_name,
        'product_price': product.price,
        'product_description': product.description if hasattr(product, 'description') else ''
    }
    return render(request, 'product_details.html', context)
