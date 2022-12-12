import os

from root.settings import BASE_DIR


def delete_main_photo(model, pk):
    if model.objects.get(id=pk).image.url:
        image_url = model.objects.get(id=pk).image.url
        os.remove(BASE_DIR + image_url)


def delete_all_photos(model, object_pk, content_type_pk):
    if model.objects.filter(object_id=object_pk, content_type_id=content_type_pk).exists():
        images_of_cpu = model.objects.filter(object_id=object_pk, content_type_id=content_type_pk)
        for item in images_of_cpu:
            os.remove(BASE_DIR + item.image.url)
            item.delete()
