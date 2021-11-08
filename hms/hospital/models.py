from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiology','Cardiology'),
('Dermatology','Dermatology'),
('Emergency Medicine','Emergency Medicine '),
('Allergy','Allergy'),
('Opthamology','Opthamology'),

]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=40,choices=departments,default='Cardiology')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



