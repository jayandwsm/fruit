from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('分类名称',max_length=30,null=False)
    desc = models.CharField('商品描述',max_length=200,default='商品描述')
    isdelete = models.BooleanField('删除',default=False)

    def __str__(self):
        return self.title
class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    desc = models.CharField('描述',max_length=200,null=False)
    unit = models.CharField('单位',max_length=10,null=False)
    picture = models.ImageField('商品图片',max_length=300,upload_to='static/image/goods',default='1.jpg')
    detail = models.CharField('详情',max_length=1000,default='商品详情')
    isdelete = models.BooleanField('删除',default=False)
    type = models.ForeignKey(GoodsType)

    def __str__(self):
        return self.title

    def get_url(self):
        return '/detail/?goodid={}'.format(self.id)












