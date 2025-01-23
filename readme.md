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
