from django.db import models

# Create your models here.
class Account(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField(null=True)
    # profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    about=models.TextField(null=True)
    phone=models.BigIntegerField(null=True)
    avatar=models.ImageField('userpicture', blank=True,null=True, upload_to='media/')
    # image kullanıcaksan yapılacaklar
    # 1 - pillow paketini kur              
    #       python -m pip install Pillow
    # 2 - settings.py a ekle     
    #       MEDIA_URL = 'media/
    # 3 - urls.py a ekle
            # from django.conf import settings
            # from django.conf.urls.static import static
            # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    account=models.OneToOneField(Account,on_delete=models.DO_NOTHING)
    # CASCADE       primary silindiğinde foraign de silinir
    # set_NULL      null olarak günceller
    # DO_NOTHING    field olduğu gibi kalır 
    # SET_DEFAULT   istenilen bir değer atanır
    # PROTECT       silmeye izin vermiyo

    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='profile about user'
        verbose_name_plural='users profile'

class Adress(models.Model):
    name=models.CharField(max_length=20)
    adress=models.TextField(null=True)
    account=models.ForeignKey(Account,null=True,on_delete=models.CASCADE)

    # account=models.ForeignKey(Account,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    productname=models.CharField(max_length=20)
    account=models.ManyToManyField(Account)

    def __str__(self):
        return self.productname


# class basket(models.Model):
#     account=models.ForeignKey(Account)
#     product=models.ForeignKey(Product)




