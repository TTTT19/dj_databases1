from django.shortcuts import render
import sqlite3 as lite

SLUG_name = 'iphone-x'


def show_catalog(request):
    sort_by = request.GET.get('sort_by', '')
    template = 'catalog.html'
    con = lite.connect('db.sqlite3')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM phones_phone")
        rows = cur.fetchall()
        items = []
        for row in rows:
            new = {'name': row[1], 'price': row[2], 'image': row[3], 'slug': row[6]}
            items.append(new)

    items_by_price = sorted(items, key=lambda key: key['price'], reverse=True)
    items_by_name = sorted(items, key=lambda key: key['name'], reverse=False)

    context = {'items': items, 'sort_by': sort_by, 'items_by_name': items_by_name, 'items_by_price': items_by_price}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    con = lite.connect('db.sqlite3')
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM phones_phone WHERE SLUG LIKE '{slug}'")
        rows = cur.fetchall()
        for row in rows:
            item = {'name': row[1], 'price': row[2], 'image': row[3], 'slug': row[6]}
    context = {'item': item}
    return render(request, template, context)
