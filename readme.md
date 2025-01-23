# Chatbot For Website

## Introduction

This project is a Django-based website that displays articles and integrates a chatbot using Google's Gemini API. The chatbot provides intelligent answers by using the displayed article's content as context.

## Features

Display articles from an external JSON file.
Chatbot that provides answers based on the article content.
Clean and responsive design with a chatbot section on the right-hand side of the article.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Your Google Gemini API Key

1. Obtain your API key from Google Generative AI.
2. Paste the API in `./ArticleSite/ArticleSite/settings.py` - line 24: `GENAI_API_KEY = ''`

### 5. Run the Server

1. `cd ArticleSite`
2. `python manage.py runserver`
3. Open your browser and navigate to: `http://127.0.0.1:8000/article/1/`
4. Note: The main page will show nothing at this moment

### 6. File Structure

[view in full screen mode]

```NaN
chatbot_for_website/
├── ArticleSite/
│   ├── articles/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── articles/
│   │   │   │   └── article.html
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── data.json            # Articles data file
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py              # URL routes
│   │   ├── views.py             # Backend logic
│   │   
│   ├── ArticleSite/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │
│   ├── db.sqlite3               # For Database (not used in this project)
│   ├── manage.py                # Django command-line utility
├── requirements.txt             # Dependencies
├── readme.md                    # readme file


```
