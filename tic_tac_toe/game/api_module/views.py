from django.http import JsonResponse

def borad_update_api_view(request):
    # Your API logic here
    print('>>> request type', request.method)
    data = {'message': 'API call successful'}
    return JsonResponse(data)
