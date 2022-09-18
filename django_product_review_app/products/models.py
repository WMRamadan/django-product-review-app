from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.shortcuts import reverse
from autoslug import AutoSlugField
from django_product_review_app import utils


class Category(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.pk is None:
			old_instance = Category.objects.filter(name__iexact=self.name)
			if old_instance:
				existing_model = old_instance.first()
				existing_model.is_deleted = False
				existing_model.name = self.name
				existing_model.save()
			else:
				super(Category, self).save(*args, **kwargs)
		else:
			super(Category, self).save(*args, **kwargs)


class Product(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField()
	image = models.FileField(upload_to=utils.generate_unique_name, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_date = models.DateField(auto_now_add=True)
	slug = AutoSlugField(populate_from='name', unique_with='created_date')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.pk is None:
			old_instance = Product.objects.filter(name__iexact=self.name)
			if old_instance:
				existing_model = old_instance.first()
				existing_model.is_deleted = False
				existing_model.name = self.name
				existing_model.save()
			else:
				super(Product, self).save(*args, **kwargs)
		else:
			super(Product, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("product", kwargs={'slug': self.slug})


class Review(models.Model):
	RATING_CHOICES = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
	)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	content = models.TextField()
	rating = models.PositiveIntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_date = models.DateField(auto_now_add=True)
