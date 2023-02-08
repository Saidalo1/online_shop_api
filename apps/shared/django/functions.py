import os

from PIL import Image, ImageChops

from root.settings import BASE_DIR


# Delete default image of object
def delete_main_photo(model, pk):
    item = model.objects.filter(id=pk)
    if item.exists():
        try:
            default_image_url = model.objects.get(id=pk).image.url
            os.remove(str(BASE_DIR) + default_image_url)
        except:
            pass


# Delete all images of object
def delete_all_photos(model, object_pk):
    images_of_cpu = model.objects.filter(product_id=object_pk)
    if images_of_cpu.exists():
        for item in images_of_cpu:
            try:
                os.remove(str(BASE_DIR) + item.image.url)
            except:
                pass
            item.delete()


# Sort default image dirs of products by name
def upload_image_product_url(instance, filename):
    return f'product/{instance.name}-product/images/default-image/{filename}'


# Sort other images dirs of products
def upload_other_images_product_url(instance, filename):
    return f'product/{instance.name}-product/images/{filename}'


# Check difference between two images
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
