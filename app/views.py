from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .crud import *
from .models import *


@require_http_methods(["GET"])
@tryexception
def read_cars_view(request, user_id):
    cars = Cars.objects.filter(owner=user_id).all()

    return JsonResponse({'cars': [
        {
            'car_name': car.name,
            'car_number': car.number
        }
        for car in cars]
    }, status=200)


@csrf_exempt
@require_http_methods(["POST"])
@tryexception
def create_car_view(request):
    data = json.loads(request.body)
    owner = Users.objects.get(id=data['owner_id'])
    new_car = Cars.objects.create(
        name=data['car_name'],
        number=data['car_number'],
        owner=owner
    )

    return JsonResponse({
        'car_id': new_car.id
    }, status=201)


@csrf_exempt
@require_http_methods(["PUT"])
@tryexception
def update_car_view(request, car_id):
    data = json.loads(request.body)
    car = Cars.objects.get(id=car_id)
    car.name = data['car_name']
    car.number = data['car_number']
    car.save()

    return JsonResponse({
        'car_id': car.id
    }, status=200)


@csrf_exempt
@require_http_methods(["DELETE"])
@tryexception
def delete_car_view(request, car_id):
    car = Cars.objects.get(id=car_id)
    car.delete()
    return JsonResponse({'message': 'Car deleted successfully'}, status=200)


@require_http_methods(["GET"])
@tryexception
def read_service_view(request, car_id):
    services = Service.objects.filter(car_id=car_id).all()
    service_data = []

    for service in services:
        service_dict = {
            'car_id': service.car_id,
            **{field.name: getattr(service, field.name) for field in Service._meta.fields if
               field.name != 'id' and field.name != 'car' and getattr(service, field.name) is not None}
        }
        service_data.append(service_dict)

    return JsonResponse({'service': service_data}, status=200)


@csrf_exempt
@require_http_methods(["POST"])
@tryexception
def create_service_view(request):
    data = json.loads(request.body)

    new_service = Service.objects.create(
        **{field.name: data.get(field.name) for field in Service._meta.fields if
           field.name != 'id' and field.name != 'car_id'},
        car_id=data['car_id']
    )

    return JsonResponse({
        'service_id': new_service.id
    }, status=201)


@csrf_exempt
@require_http_methods(["DELETE"])
@tryexception
def delete_service_view(request, service_id):
    service = Service.objects.get(id=service_id)
    service.delete()
    return JsonResponse({'message': 'Service deleted successfully'}, status=200)
