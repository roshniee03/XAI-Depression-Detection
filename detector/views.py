import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .predict import predict

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        data  = json.loads(request.body)
        result = predict(data['text'])
        return JsonResponse(result)