from .models import Category
def global_data(request):

    data = {
        'categoryData':Category.objects.all()
    }
    return data