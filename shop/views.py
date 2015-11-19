# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from .models import Item, Category, Order, OrderItem, Bug, Profile, Comment
import json
import xlrd

def index(request):
    return render(request, 'shop/index.html', {'categories': parse_categories()[0]['content']})

def search_item(request):
    if request.method == 'GET':
        search_name = request.GET['s']
    else:
        search_name = request.POST['search_item']

    if 'comp' not in request.session:
        request.session['comp'] = []

    if request.method == 'POST':
        if request.POST['type'] == 'cart':
            manage_cart(request)
        else:
            manage_comp(request)

    return render(request, 'shop/catalog.html', {'categories': parse_categories()[0]['content'], 'current_category': 'search', 'items': Item.objects.filter(name__contains=search_name), 'cart': json.dumps(request.session['cart']), 'comp': json.dumps(request.session['comp'])})

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = '/'

    template_name = 'shop/signin.html'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/signin'

    template_name = 'shop/signup.html'

    def form_valid(self, form):
        form.save()

        return super(RegisterFormView, self).form_valid(form)

def profile(request):
    if request.method == 'POST':
        Profile.objects.update_or_create(user_id=request.user.id, address=request.POST.get('address', ''), pay_method=request.POST.get('pay_method', ''))

        u = request.user
        u.first_name = request.POST.get('first_name', '')
        u.last_name = request.POST.get('last_name', '')
        u.email = request.POST.get('email', '')
        u.save()

    try:
        p = Profile.objects.get(user_id=request.user.id)
    except:
        p = {'address': '', 'pay_method': ''}

    return render(request, 'shop/profile.html', {'profile': p})

def compare(request, category_id=0):
    if category_id is None:
        category_id = 0

    manage_comp(request)
    items = Item.objects.filter(id__in=request.session['comp'])
    categories = []
    if category_id == 0:
        for item in items:
            if item.category_id not in categories:
                categories.append(item.category_id)
        if (len(categories) == 0):
            return render(request, 'shop/compare.html', {'mode': 'none'})
        if (len(categories) > 1):
            return render(request, 'shop/compare.html', {'mode': 'cat_list', 'categories': Category.objects.filter(id__in=categories)})
        if (len(categories) == 1):
            compare(request, categories[0])
            return render(request, 'shop/compare.html')

    cat_items = []
    items = Item.objects.filter(id__in=request.session['comp'])
    for item in items:
        if str(item.category_id) == str(category_id):
            cat_items.append(item)

    descs = {}
    max_size = 0
    for item in cat_items:
        split_desc = item.desc.split(', ')
        if (len(split_desc) > max_size):
            max_size = len(split_desc)
        descs[item.name] = split_desc

    descs_arr = []
    for i in range(max_size):
        descs_i = []
        for item in cat_items:
            if i >= len(descs[item.name]):
                curr_desc = ''
            else:
                curr_desc = descs[item.name][i]
            descs_i.append(curr_desc)
        descs_arr.append(descs_i)
        descs_i = []

    return render(request, 'shop/compare.html', {'items': cat_items, 'descs': descs_arr})

def cart(request):
    manage_cart(request)

    return render(request, 'shop/cart.html', {'cart': {Item.objects.get(id=int(key)): value for key, value in request.session['cart'].items()}})

def catalog(request, category_id=0):
    if category_id is None:
        category_id = 0

    if 'comp' not in request.session:
        request.session['comp'] = []

    if request.method == 'POST':
       if request.POST['type'] == 'cart':
           manage_cart(request)
       else:
           manage_comp(request)
    else:
        if 'cart' not in request.session:
            request.session['cart'] = {}
        if 'comp' not in request.session:
            request.session['comp'] = []

    items = []

    category_list = parse_categories()

    cur_category = category_list[int(category_id)]

    for i in range (len(cur_category['content'])):
        add_category = cur_category['content'][i]
        items.append({'id': add_category['id'], 'name': add_category['name'], 'price': None })

    if len(items) == 0:
        items = Item.objects.filter(category=category_id)

    return render(request, 'shop/catalog.html', {'categories': parse_categories()[0]['content'], 'current_category': cur_category, 'items': items, 'cart': json.dumps(request.session['cart']), 'comp': json.dumps(request.session['comp'])})

def item(request, category_id, item_id):
    users = []
    if request.method == 'POST':
        c = Comment(
            user_id=request.user.id,
            item_id=item_id, comment=request.POST['comment'], rating=request.POST['item_rate'])
        c.save()
        #users.append(User.objects.get(id=request.user))

    #manage_cart(request)

    item = Item.objects.get(id=item_id)
    desc = item.desc.split(', ')
    if desc[0] == '':
        desc = None

    return render(request, 'shop/item.html', {
        'categories': parse_categories()[0]['content'], 'item': item,
        'desc': desc, 'cart': request.session['cart'], 'comm': Comment.objects.filter(item_id=item_id)})

def order(request):
    force_access = False
    if request.method == 'GET':
        if request.session['prev_posted'] == False:
            force_access = True
    else:
        request.session['prev_posted'] = False
        if request.POST.get('post_order', 'False') == 'True':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            address = request.POST['address']
            pay_method = request.POST['pay_method']
            o = Order(first_name=first_name, last_name=last_name, email=email, address=address, pay_method=pay_method)
            o.save()
            for item, count in request.session['cart'].items():
                oi = OrderItem(count=int(count))
                oi.order_id = o.id
                oi.item_id = int(item)
                oi.save()
            request.session['prev_posted'] = True
            request.session['cart'] = {}

    try:
        p = Profile.objects.get(user_id=request.user.id)
    except:
        p = {'address': '', 'pay_method': ''}

    return render(request, 'shop/order.html', {'categories': parse_categories()[0]['content'], 'cart': request.session['cart'], 'profile': p, 'prev_posted': request.session['prev_posted'], 'force_access': force_access})

def bugreport(request):
    if 'HTTP_REFERER' not in request.META:
        referer_url = request.build_absolute_uri()
    else:
        referer_url = request.META['HTTP_REFERER']

    if request.method == 'POST':
        bug = Bug(bug_url=request.POST['bug_url'], bug_desc=request.POST['bug_desc'], bug_rate=request.POST['bug_rate'])
        bug.save()

    return render(request, 'shop/bugreport.html', {'referer_url': referer_url})

def adm(request):
    return render(request, 'shop/admin.html')

def manage_cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']

    if request.method == 'POST':
        if request.POST['action'] == 'add':
            cart[request.POST['item_id']] = 1
            request.session.modified = True
        elif request.POST['action'] == 'remove':
            if cart:
                if request.POST['item_id'] in cart:
                    cart.pop(request.POST['item_id'], None)
                    request.session.modified = True
        elif request.POST['action'] == 'change_count':
            cart[request.POST['item_id']] = request.POST['new_count']
            request.session.modified = True
    print(request.session['comp'])

def manage_comp(request):
    if 'comp' not in request.session:
        request.session['comp'] = []

    comp = request.session['comp']

    if request.method == 'POST':
        if request.POST['action'] == 'add':
            comp.append(request.POST['item_id'])
            request.session.modified = True
        elif request.POST['action'] == 'remove':
            if comp:
                if request.POST['item_id'] in comp:
                    comp.remove(request.POST['item_id'])
                    request.session.modified = True

def parse_categories():
    categories = [{'id': None, 'name': None, 'content': []} for i in range(len(Category.objects.all()) + 1)]

    for c in Category.objects.all():
        index = c.id
        name = c.name
        path = list(map(int, c.location.split(',')))

        if categories[index]['name'] is None:
            categories[index]['id'] = index
            categories[index]['name'] = name

        categories[path[len(path) - 1]]['content'].append(categories[index])

    return categories



def parse_xls():
    rb = xlrd.open_workbook('c:/shop_site/shop/price-list.xls', formatting_info=True)
    sheet = rb.sheet_by_index(0)

    cat_id = 0
    cat_path = [0]

    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        if rownum > 1:
            level = sheet.rowinfo_map[rownum - 1].outline_level
        else:
            level = 0

        if row[3] != '':
            if row[1] == '':
                cat_path.append(cat_id)

                sub = level - (len(cat_path)) + 1
                if sub != 0:
                    cat_path = cat_path[:sub]

                c = Category(name=row[3][0] + row[3][1:].lower(), location=','.join(list(map(str, cat_path))))
                c.save()

                cat_id += 1
            else:
                full_desc = row[3].split(',')
                name = full_desc[0]
                desc = ', '.join(full_desc[1:])

                if (row[6] != ''):
                    price = int(row[6])
                    i = Item(name=name, desc=desc, price=price)
                    i.category_id = cat_id
                    i.save()