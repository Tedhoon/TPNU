from django.db import models

class DeliveryList(models.Model):
    title = models.CharField(max_length=100)
    # deliveryCondition = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    
    # menuname = models.TextField()
    # menunotion = models.TextField()
    # menuprice = models.TextField()


    description = models.CharField(max_length = 150)
    # deliveryPrice = models.CharField(max_length = 150)
    # deliveryTime = models.CharField(max_length = 150)
    # paymentMethod = models.CharField(max_length = 150)

    # restaurant_Info = models.CharField(max_length = 150)
    # restaurant_OpenTIme = models.CharField(max_length = 150)
    
    # **사업자정보**
    # 상호명
    # 사업자등록번호

    # 원산지정보

    def __str__(self):
        return self.title

class DeliveryGroup(models.Model):
    pass

class DeliveryService(models.Model):
    pass
    