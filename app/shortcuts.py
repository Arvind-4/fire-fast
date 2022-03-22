from slugify import slugify

def get_slug(text: str):
    return slugify(text)