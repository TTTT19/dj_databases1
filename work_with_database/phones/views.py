from django.shortcuts import render
from phones.models import Phone



def show_catalog(request):
    sort_by = request.GET.get('sort_by', '')
    template = 'catalog.html'
    rows = Phone.objects.all()
    items = []
    for row in rows:
        new = {'name': row.name, 'price': row.price, 'image': row.image, 'slug': row.slug}
        items.append(new)
    items_by_price = sorted(items, key=lambda key: key['price'], reverse=True)
    items_by_name = sorted(items, key=lambda key: key['name'], reverse=False)
    context = {'items': items, 'sort_by': sort_by, 'items_by_name': items_by_name, 'items_by_price': items_by_price}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    rows = Phone.objects.filter(slug=slug)
    for row in rows:
        item = {'name': row.name, 'price': row.price, 'image': row.image, 'slug': row.slug}
    context = {'item': item}
    return render(request, template, context)
