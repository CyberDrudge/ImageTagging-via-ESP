import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1000000000000000)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'images/{new_filename}/{final_filename}'
