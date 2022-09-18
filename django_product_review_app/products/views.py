from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Review
from .forms import ReviewForm
from django.db.models import Count
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

def home_view(request):
	product_list = Product.objects.all().annotate(review_count=Count('review'))
	page = request.GET.get('page', 1)
	paginator = Paginator(product_list, 4)
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	context = {
		'products': products,
		'categories': Category.objects.all()
	}
	

	return render(request, "home.html", context)

def product_detail_view(request, slug):
	form = ReviewForm()
	context = {
		'product': Product.objects.get(slug=slug),
		'reviews': Review.objects.filter(product__slug=slug),
		'form': form
	}
	return render(request, "product-page.html", context)

def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        content = form.cleaned_data['content']
        author = request.user
        review = Review()
        review.product = product
        review.author = author
        review.rating = rating
        review.content = content
        review.created_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'product-page.html', {'product': product})
