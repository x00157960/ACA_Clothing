from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView
from django.db.models import Q
from .models import Category, Product

class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list

    

def product_list(request, category_id=None):
    category = None
    products = Product.objects.all()
    ccat = Category.objects.annotate(num_products=Count('products'))
    if(category_id):
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'products.html',
                    {'products': products,
                    'countcat':ccat})
 
def productdetail(request,id):
    product = Product.objects.get(id = id)
    return render(request, 'product.html', {'product': product})

def SignupView(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})


def SigninView(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form =AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form })

def SignoutView(request):
    logout(request)
    return redirect('home')


