from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from .data_preprocess import predict_class, preprocess_text
 
def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        # Calling the predict_class function to get the predicted class
        predicted_class = predict_class(text)

        # Mapping the predicted class to sentiment class
        if predicted_class > 0.5:
            sentiment_class = 'Negative'
        elif predicted_class == 0.5:
            sentiment_class = 'Neutral'
        else:
            sentiment_class = 'Positive'

        context = {
            'class': sentiment_class,
        }
        return render(request, 'core/analyze_sentiment.html', context)
    else:
        return render(request, 'core/analyze_sentiment.html')

@api_view(['POST','GET'])    
def home(request):
    return render(request, 'core/home.html')

def info(request):
    return render(request, 'core/info.html')


    
