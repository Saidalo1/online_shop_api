import os
from datetime import datetime

from PIL import Image, ImageChops

from root.settings import BASE_DIR


# Delete default image of object
def delete_main_photo(model, pk):
    if model.objects.filter(id=pk).exists() and model.objects.get(id=pk).image.url:
        image_url = model.objects.get(id=pk).image.url
        os.remove(BASE_DIR + image_url)


# Delete all images of object
def delete_all_photos(model, object_pk, content_type_pk):
    if model.objects.filter(object_id=object_pk, content_type_id=content_type_pk).exists():
        images_of_cpu = model.objects.filter(object_id=object_pk, content_type_id=content_type_pk)
        for item in images_of_cpu:
            os.remove(BASE_DIR + item.image.url)
            item.delete()


# Sort image dirs of cpu by date and slug
def upload_name_cpu(instance, filename):
    date = datetime.now().strftime('%Y/%m/%d')
    return f'csp/cpu/images/{date}/default-image/{instance.slug}/{filename}'


# Sort image dirs of video_card by date and slug
def upload_name_video_card(instance, filename):
    date = datetime.now().strftime('%Y/%m/%d')
    return f'csp/video-card/images/{date}/default-image/{instance.slug}/{filename}'


def has_difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    if image_1.size == image_2.size:
        result = ImageChops.difference(image_1, image_2)
        if result.getbbox() is None:
            # difference not found
            return False
    # difference found
    return True
