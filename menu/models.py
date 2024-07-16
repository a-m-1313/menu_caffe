from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    CAFEE = 'c'
    ICEPACK = 'i'
    DESSERT = 'd'
    SNACK = 's'
    SMOOTHIE ='s'
    MOCKTAILE ='m'
    LIST_NAME = [
        (CAFEE, 'Caffe'),
        (ICEPACK, 'IcePack'),
        (DESSERT, 'Dessert'),
        (SNACK, 'Snack'),
        (SMOOTHIE, 'Smoothie'),
        (MOCKTAILE, 'Mocktile'),
    ]
    name = models.CharField(max_length=225, verbose_name=_('name'), unique=True)
    description = models.TextField(verbose_name=_('description'), blank=True)
    top_product = models.ForeignKey('product', on_delete=models.CASCADE , related_name='+'
                                    , blank=True, null=True, verbose_name=_('top_product'))

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category' , verbose_name=_('category'))
    description = models.TextField(verbose_name=_('description'))
    name = models.CharField(max_length=225, verbose_name=_('name'))
    price = models.IntegerField(validators=[MinValueValidator(0), ], verbose_name=_('price'))
    image = models.ImageField(upload_to='media/snack_images/', verbose_name=_('image'), blank=True)

    def __str__(self):
        return self.name
    
    def media(self):
        if self.image:
            return getattr(self.image, 'url', None)
        return 'static/Untitled-1.jpg'
        
       
    
        

        


    
# class Snack(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#     #category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='snack_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/snack_images/')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_snack')


#     def __str__(self):
#         return self.name

#     def media(self):
#         return getattr(self.image, 'url', None)


# class IcePack(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#     #category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='icepack_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/icepack_images/')    
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_icepack')


#     def __str__(self):
#         return self.name

#     def media(self):
#         return getattr(self.image, 'url', None)


# class Caffe(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#     #category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='caffe_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/caffe_images/')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_caffe')

#     def __str__(self):
#         return self.name



#     def media(self):
#         if self.image:
#             return getattr(self.image, 'url', None)

# class Mocktail(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#    # category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='mocktail_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/mocktail_images/')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_mocktail')
#     def __str__(self):
#         return self.name


#     def media(self):
#         return getattr(self.image, 'url', None)


# class Smoothie(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#    #category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='smoothie_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/smoothie_images/')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_smoothie')

#     def __str__(self):
#         return self.name


#     def media(self):
#         return getattr(self.image, 'url', None)


# class Dessert(models.Model):
#     name = models.CharField(max_length=225)
#     description = models.TextField()
#    # category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='dessert_categories')
#     price = models.IntegerField(validators=[MinValueValidator(0), ])
#     image = models.ImageField(upload_to='media/dessert_images/')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_dessert')

#     def __str__(self):
#         return self.name
    

#     def media(self):
#         return getattr(self.image, 'url', None)







