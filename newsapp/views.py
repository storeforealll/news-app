from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from newsapi import NewsApiClient
from .forms import NewsFilterForm
from .models import NewsQuery

def news_list(request):
    # Initialize with default values
    country = 'us'
    category = 'general'
    form = NewsFilterForm(request.GET or None)
    articles = []
    error_message = None

    if form.is_valid():
        country = form.cleaned_data['country']
        category = form.cleaned_data['category']
        
        # Log the query
        NewsQuery.objects.create(
            country=country,
            category=category
        )

        # Create a cache key
        cache_key = f'news_{country}_{category}'
        
        # Try to get cached data first
        articles = cache.get(cache_key)
        
        if not articles:
            try:
                newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
                response = newsapi.get_top_headlines(
                    country=country,
                    category=category,
                    page_size=20
                )
                articles = response['articles']
                # Cache for 30 minutes
                cache.set(cache_key, articles, 1800)
            except Exception as e:
                error_message = "Could not fetch news. Please try again later."
                print(f"News API Error: {str(e)}")

    context = {
        'articles': articles,
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'news_list.html', context)