from django.db import models
from django.forms import ModelForm
from django import forms

class Item(models.Model):
	name = models.CharField(max_length=200)
	desc = models.CharField(max_length=5000)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	pub_date = models.DateTimeField('date published',auto_now_add=True)
	def __unicode__(self):
		return self.name

class Catagories(models.Model):
	item = models.ForeignKey(Item)
	ctg = models.CharField(max_length=200)
	def __unicode__(self):
		return self.ctg




class Pic(models.Model):
    picfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    item = models.ForeignKey(Item)

class PicForm(forms.Form):
    picfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ['name', 'desc', 'price']
