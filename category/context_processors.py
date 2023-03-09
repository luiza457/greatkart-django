# takes a request as an argument 
# returns a dict of data as a context 
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)