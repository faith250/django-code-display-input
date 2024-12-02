from django.http import JsonResponse
from .models import ProductInfo

def get_filtered_data(request):
    # Example filter logic
    color = request.GET.get('color', None)
    products = ProductInfo.objects.all()
    if color:
        products = products.filter(color=color)
    product_list = list(products.values())
    return JsonResponse(product_list, safe=False)
