from django.shortcuts import render
from django.template import loader
from appone.models import UserProfile
from django.http import HttpResponse
from django.db.models import Max
from django.db.models import Min
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):

    template = loader.get_template('index.html')

    product = UserProfile.objects.all()

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/productDetails/
def userProfileDetails(request):
    #creating object
    template=loader.get_template('productDetails.html')
    #talk to database
    product = UserProfile.objects.all()
    p={'product':product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/conatinsProductName/
# select * from tablename where fieldname like 'SamsungFlip3';
'''__contains'''
def conatinsProductName(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_name__contains="Samsung")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))


# http://127.0.0.1:8000/iconatinsProductName/
'''__icontains'''
def iconatinsProductName(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_name__icontains="Apple")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/greaterThanProductName/
# select * from tablename where fieldname > 50000;
'''__gt'''
def greaterThanProductName(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_cost__gt="50000")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))


# http://127.0.0.1:8000/greaterThanEqualProductName/
'''__gte'''
def greaterThanEqualProductName(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_cost__gte ="50000")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/productNameStartsWith/
'''__startswith'''
def productNameStartsWith(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_name__startswith="Apple")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/productNameEndsWith/
'''__endsWith'''
def productNameEndsWith(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_name__endswith="Pro")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

'''__exact'''
# def productNameExact(request):

#     template = loader.get_template('userProfileDetails.html')

#     details = UserProfile.objects.filter(product_name__exact="apple")
#     print(details)
#     print(type(details))

#     d = {'details' : details}

#     return HttpResponse(template.render(context=d))

# http://127.0.0.1:8000/productNameExact/
from django.db.models import Func, F
def productNameExact(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.annotate(
        product_name_binary=Func(
            F('product_name'), function='BINARY')).filter(product_name_binary__exact="iPhone15pro")
    
    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/iproductNameExact/
'''__iexact'''
def iproductNameExact(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(product_name__iexact="iphone15Pro")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/userNameExclude/
'''exclude()'''
def userNameExclude(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.exclude(user_name = "manjil123")
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/productNamesExcludeOr/
''' exclude with | operator '''
from django.db.models import Q
def productNamesExcludeOr(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.exclude(Q(product_name="Apple 14 mini") | Q(product_name="Apple 14 Pro"))
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/productNamesExcludeAnd/
''' exclude with | operator '''
from django.db.models import Q
def productNamesExcludeAnd(request):

    template = loader.get_template('productDetails.html')

    product = UserProfile.objects.filter(Q(product_name__startswith="iPhone15pro") & Q(user_name__startswith="sai kiran"))
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/maxProductPrice/
''' product_cost__max'''
def maxProductPrice(request):
    template = loader.get_template('productDetails.html')

    max_price = UserProfile.objects.aggregate(Max('product_cost'))['product_cost__max']

    product = UserProfile.objects.filter(product_cost=max_price )

    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/minProductPrice/
''' product_cost__min'''
def minProductPrice(request):
    template = loader.get_template('productDetails.html')

    min_price = UserProfile.objects.aggregate(Min('product_cost'))['product_cost__min']

    product = UserProfile.objects.filter(product_cost=min_price )

    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/valuesMethod/
'''Only value listed can be called, return type dictonary'''
def valuesMethod(request):

    template = loader.get_template('productDetails.html')
    product = UserProfile.objects.all().values('user_name', 'product_name', 'product_cost')
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))


# http://127.0.0.1:8000/values_listMethod/
'''Only value listed can be called, return type tuple'''
def values_listMethod(request):

    template = loader.get_template('productDetails.html')
    product = UserProfile.objects.all().values_list('user_name', 'product_name', 'product_cost', named=True)
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/orderByCostDesc/
'''Descending order by'''
def orderByCostDesc(request):

    template = loader.get_template('productDetails.html')
    product = UserProfile.objects.all().order_by('product_cost') 
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/orderByCostAscen/
'''Ascending order by'''
def orderByCostAscen(request):

    template = loader.get_template('productDetails.html')
    product = UserProfile.objects.all().order_by('-product_cost') 
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/insertCreate/
'''insert data by create'''
def insertCreate(request):

    template = loader.get_template('insertCreate.html')
    product = UserProfile.objects.create(user_name='manjil1', user_contact='682222323', user_email='manjil1@gmail.com', product_name='SamsungFlip', product_cost='30000.00')
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/insertBySave/
'''Insert by Save method'''
def insertBySave(request):

    template = loader.get_template('insertBySave.html')
    product = UserProfile(user_name='manjil2323', user_contact='682222222', user_email='manjil2323@gmail.com', product_name='SamsungFlip2', product_cost='40000.00')
    product.save()
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))

# http://127.0.0.1:8000/updateRecords/
'''UpdateRecords'''
def updateRecords(request):

    template = loader.get_template('updateRecords.html')
    product = UserProfile.objects.get(id=13)
    product.user_name = 'manjil33'
    product.product_name = 'Samsung Flip'
    product.save()
    print(product)
    print(type(product))

    d = {'product' : product}

    return HttpResponse(template.render(context=d))

# http://127.0.0.1:8000/bulkCreate/
'''bulkCreate'''
def bulkCreate(request):
    template = loader.get_template('bulkCreate.html')
    products = [
    UserProfile(user_name='manjil63', user_contact=80000000, user_email='max@gmail.com',product_name='Apple 14 Max',product_cost=50000),
    UserProfile(user_name='manjil62', user_contact=80700, user_email='max@gmail.com',product_name='Apple 15 Max',product_cost=56000),
    UserProfile(user_name='manjil64', user_contact=85000000, user_email='max@gmail.com',product_name='Apple 16 Max',product_cost=57000),
    UserProfile(user_name='manjil65', user_contact=80000000, user_email='max@gmail.com',product_name='Apple 17 Max',product_cost=59000),
    UserProfile(user_name='manjil66', user_contact=500000000, user_email='max@gmail.com',product_name='Apple 17 Pro Max',product_cost=90000),]  

    product = UserProfile.objects.bulk_create(products)
    print(product)
    print(type(product))

    p = {'product' : product}

    return HttpResponse(template.render(context=p))


def about(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render())

def contactus(request):
    template = loader.get_template('contactus.html')

    return HttpResponse(template.render())

@csrf_exempt
def search_results(request):
    
    query = request.GET.get('q', '')
    if query:
        products = UserProfile.objects.filter(product_name__icontains=query)
    else:
        products = UserProfile.objects.none()
    return render(request, 'search_result.html', {'products': products})









 



   
