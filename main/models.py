from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from datetime import date,datetime,timedelta

class CustomUser(AbstractUser):
   information = models.CharField(max_length=50 , null=True)
   website = models.CharField(max_length=50 , null=True)
   phone =  models.CharField(max_length=50 , null=True)
   choise = models.CharField(max_length=15,null=True)
   img = models.FileField(upload_to='images/')
   cover = models.FileField(upload_to='images/')
   
   def __str__(self):
        return self.username
   def get_absolute_url(self):
        return f'/'
    
class Guide(models.Model):
   
   content = RichTextField(null=True)
   photo = models.FileField(upload_to='images/')
   title = models.CharField(max_length=50)
   description = models.CharField(max_length=100)
   about = models.CharField(max_length=300)
   duration = models.CharField(max_length=50)
   meeting_point = models.CharField(max_length=50)
   transport = models.CharField(max_length=50)
   whats_included = models.CharField(max_length=50)
   price = models.FloatField(max_length=50)
   extra = models.CharField(max_length=50)
   restriction = models.CharField(max_length=50)
   itinerary = models.CharField(max_length=50)
   user_id = models.IntegerField()
   
   def __str__(self):
        return self.title
   def get_absolute_url(self):
        return f'/' 
   
class Order(models.Model):

   tur_id = models.ForeignKey(Guide ,on_delete= models.CASCADE,null=True) # tur idsi
   user_id = models.ForeignKey(CustomUser ,on_delete= models.CASCADE ,null=True) # Sifarishi basanin idsi
   utesdiq = models.IntegerField(null=True)
   gtesdiq = models.BooleanField(null=True)
   gstatus = models.IntegerField(null=True)
   guide_id = models.IntegerField(null=True) #turu yaradanin idsi
   guide_photo = models.FileField(upload_to='images/',null=True)
   guide_username = models.CharField(max_length=50,null=True)
   guide_phone = models.CharField(max_length=50,null=True)
   guide_information = models.CharField(max_length=50,null=True)
   guide_cover = models.FileField(upload_to='images/',null=True)
   active = models.BooleanField(default=True,verbose_name='active')
   
   def get_absolute_url(self):
        return f'/'
    
#    @property
#    def diff(self):
#      now = datetime.now()
#      td = timedelta(minutes=1)
#      d = datetime.now() + td



     