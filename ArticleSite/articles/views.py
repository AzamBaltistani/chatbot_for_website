import json
from django.shortcuts import render

def article_view(request, article_id):
    with open('articles/data.json', 'r') as file:
        data = json.load(file)
        article = next((a for a in data["articles"] if a["id"] == article_id), None)
    return render(request, 'articles/article.html', {'article': article})



import google.generativeai as genai
from django.http import JsonResponse
from django.conf import settings
import json

genai.configure(api_key=settings.GENAI_API_KEY)

def chatbot_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('message', '')
        article_id = data.get('article_id', '')  # Get the article ID from the request

        print(f"got article id is; {article_id}")
        
        # Load the article content
        with open('articles/data.json', 'r') as file:
            articles = json.load(file)["articles"]
            print("All articles: ", articles)
            article = next((a for a in articles if a["id"] == int(article_id)), None)

        if not article:
            return JsonResponse({'reply': 'Article not found'}, status=404)

        if user_input.strip():
            # Include the article content as context in the prompt
            prompt = f"This is the context: {article['content']}, now answer the question: {user_input}"

            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                bot_reply = response.text
            except Exception as e:
                bot_reply = f"An error occurred: {e}"

            return JsonResponse({'reply': bot_reply})

    return JsonResponse({'reply': 'Invalid request method'}, status=400)
