from django.db.models import Manager


class ProductManager(Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(count__gt=0)
