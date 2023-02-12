from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, DateTimeField
from django.urls import reverse


class TimeBaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

    class Meta:
        abstract = True
