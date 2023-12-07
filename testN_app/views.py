

# Create your views here.
from django.http import JsonResponse
from .models import Comic, Rating
from django.views.decorators.http import require_POST
from django.db.models import Avg

@require_POST
def create_rating(request):
    comic_id = request.POST.get('comic_id')
    user_id = request.POST.get('user_id')
    value = request.POST.get('value')

    comic = Comic.objects.get(id=comic_id)
    rating, created = Rating.objects.update_or_create(
        comic=comic, 
        user_id=user_id, 
        defaults={'value': value}
    )

    # Обновление рейтинга комикса
    new_rating = Rating.objects.filter(comic=comic).aggregate(Avg('value'))['value__avg']
    comic.rating = new_rating
    comic.save()

    return JsonResponse({'message': 'Rating updated', 'new_rating': new_rating})


from django.views.decorators.http import require_GET

@require_GET
def get_comic_rating(request, comic_id):
    comic = Comic.objects.get(id=comic_id)
    return JsonResponse({'comic': comic.title, 'rating': comic.rating})

