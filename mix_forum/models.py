from django.db import models

# Create your models here.

class Train(models.Model):
    Ttype = models.CharField(max_length=20,primary_key=True)
    Tnum = models.IntegerField()

    #指定该MODEL属于哪个APP

    class Meta:
        app_label = 'mix_forum'

class Diesel(models.Model):
    D_name = models.CharField(max_length=30)
    D_first_date = models.DateTimeField()
    D_num = models.IntegerField()
    D_pic = models.BinaryField()
    D_type = models.ForeignKey('Train',on_delete=models.PROTECT)
    D_usedfor = models.NullBooleanField(db_column='''0货运,1客运,null客货两用''')

    # 指定该MODEL属于哪个APP

    class Meta:
        app_label = 'mix_forum'

class Electric(models.Model):
    E_name = models.CharField(max_length=30)
    E_first_date = models.DateTimeField()
    E_num = models.IntegerField()
    E_pic = models.BinaryField()
    E_type = models.ForeignKey('Train',on_delete=models.PROTECT)
    E_usedfor = models.NullBooleanField(db_column='''0货运,1客运,null客货两用''')
    # 指定该MODEL属于哪个APP

    class Meta:
        app_label = 'mix_forum'


class Steam(models.Model):
    S_name = models.CharField(max_length=30)
    S_first_date = models.DateTimeField()
    S_num = models.IntegerField()
    S_pic = models.BinaryField()
    S_type = models.ForeignKey('Train', on_delete=models.PROTECT)
    S_usedfor = models.NullBooleanField(db_column='''0货运,1客运,null客货两用''')
    # 指定该MODEL属于哪个APP

    class Meta:
        app_label = 'mix_forum'



