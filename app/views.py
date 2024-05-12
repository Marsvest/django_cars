from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .crud import *
from .models import Cars
import json


@require_http_methods(["GET"])
@tryexception
def get_cars_view(request, user_id):
    cars = Cars.objects.filter(owner=user_id).all()

    return JsonResponse({'cars': [
        {
            'car_name': car.name,
            'car_number': car.number
        }
        for car in cars]
    }, status=200)


@require_http_methods(["POST"])
@tryexception
def create_car_view(request):
    data = json.loads(request.body)
    new_car = Cars.objects.create(
        name=data['car_name'],
        number=data['car_number'],
        owner=request.user
    )

    return JsonResponse({
        'car_name': new_car.name,
        'car_number': new_car.number
    }, status=201)


@require_http_methods(["PUT"])
@tryexception
def update_car_view(request, car_id):
    data = json.loads(request.body)
    car = Cars.objects.get(id=car_id)
    car.name = data['car_name']
    car.number = data['car_number']
    car.save()
    return JsonResponse({
        'car_name': car.name,
        'car_number': car.number
    }, status=200)


@require_http_methods(["DELETE"])
@tryexception
def delete_car_view(request, car_id):
    car = Cars.objects.get(id=car_id)
    car.delete()
    return JsonResponse({'message': 'Car deleted successfully'}, status=200)
