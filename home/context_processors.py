from .models import CommonOption


def footer_feature(request):
    return {
        'your_site_url': CommonOption.objects.filter(key="Your site link").first().value,
        'your_site_name': CommonOption.objects.filter(key="Your site name").first().value,
        'footer_orange_text': CommonOption.objects.filter(key="Footer orange text").first().value
    }
