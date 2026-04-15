from PIL import Image


def generate_pil_image(images):
    ptl_images = []

    for img in images:
        ptl_images.append(Image.open(img))

    return ptl_images;