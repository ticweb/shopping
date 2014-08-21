from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Question
from django.http import Http404
from django.shortcuts import get_object_or_404 
from django.http import HttpResponseRedirect
from polls.models import Choice
from polls.models import Question
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from shop.models import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from decimal import *
from django.contrib.auth.forms import UserCreationForm

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
	template = loader.get_template('shop/index.html')
	admin = False
	if 'admin' in request.user.groups.values_list('name',flat=True):
		admin = True
	items = Item.objects.all()
	context = RequestContext(request, {'bob':admin,'items':items})
	return HttpResponse(template.render(context))

def index2(request):
	template = loader.get_template('shop/index.html')
	admin = False
	if 'admin' in request.user.groups.values_list('name',flat=True):
		admin = True
	items = Item.objects.all().order_by('-pub_date')
	context = RequestContext(request, {'bob':admin,'items':items})
	return HttpResponse(template.render(context))

def cart(request):
	theUser = request.user
	theCart = ""
	try:
		theCart = Cart.objects.get(user = theUser)
	except:
		theCart = Cart(user = theUser)
		theCart.save()
	allItems = Item.objects.filter(carts = theCart)
	totalPrice = Decimal(0.0)
	for item in allItems:
		totalPrice += item.price
	return render(request, 'shop/cart.html', {'items': allItems,'price':totalPrice})

def additem(request):
	theUser = request.user
	theCart = ""
	try:
		theCart = Cart.objects.get(user = theUser)
	except:
		theCart = Cart(user = theUser)
		theCart.save()
	theItemId = request.POST['itemid']
	theItem = Item.objects.get(id=theItemId)
	theItem.carts.add(theCart)
	theItem.save()
	return cart(request)



def addItem(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
	# create a form instance and populate it with data from the request:
	form = ItemForm(request.POST)
	# check whether it's valid:
	if form.is_valid():
	    # process the data in form.cleaned_data as required
	    # ...
	    new_item = form.save(commit=False)
	    pf = PicForm(request.POST, request.FILES)
	    if pf.is_valid():
	        new_item.save()
	        new_pic = Pic(picfile = request.FILES['picfile'],item =new_item)
	        new_pic.save()
	    # redirect to a new URL:
	        return HttpResponseRedirect('/shop/')
	    else:
	        return render_to_response('addItem.html', {'form':form,'pf':pf},context_instance=RequestContext(request))
	else:
	    return render_to_response('addItem.html', {'form':form,'pf':pf},context_instance=RequestContext(request))
    # if a GET (or any other method) we'll create a blank form
    else:
	form = ItemForm()
	formpic = PicForm()
    return render(request, 'addItem.html', {'form': form,'pf':formpic})


def create(request):
    if request.method == 'POST':
	form = UserCreationForm(request.POST)
	if form.is_valid():
	    new_user = form.save()
	    return HttpResponseRedirect('/shop/')
	else:
		return render_to_response('shop/create.html', {'form':form},context_instance=RequestContext(request))
    else:
	form = UserCreationForm()
    return render(request, 'shop/create.html', {'form': form})




def salePage(request, salePage):
	item = get_object_or_404(Item, pk=salePage)
	pic = Pic.objects.get(item=item)
	return render(request, 'shop/page.html', {'i': item,'pic':pic})
