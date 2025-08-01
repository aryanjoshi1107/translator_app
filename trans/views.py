from django.shortcuts import render
from googletrans import Translator



def home(request):
    return render(request,'translator_home.html')

def translate_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        text_language = request.POST.get('text_language')
        translated_language = request.POST.get('translated_language')
        
        # Check if text is provided
        if not text:
            return render(request, 'translator_home.html', {'error': 'Please enter text to translate'})
        
        print(text, text_language, translated_language)
        
        try:
            # Initialize translator and perform translation
            translator = Translator()
            result = translator.translate(text, src=text_language, dest=translated_language)
            
            # Extract the translated text from the result object
            translated_text = result.text
            print(f"Translated: {translated_text}")
            
            return render(request, 'translator_home.html', {'translatedText': translated_text})
            
        except Exception as e:
            print(f"Translation error: {e}")
            return render(request, 'translator_home.html', {'error': 'Translation failed. Please try again.'})
    
    return render(request, 'translator_home.html')