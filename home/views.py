from django.shortcuts import render
from .models import CommonOption, Counter, Testimonial


# Create your views here.
def index(request):
    banner_slogan = CommonOption.objects.filter(key="Banner slogan").first()
    about_title = CommonOption.objects.filter(key="About title").first()
    about_text = CommonOption.objects.filter(key="About text").first()
    about_image = CommonOption.objects.filter(key="About image").first()
    about_100_healthy = CommonOption.objects.filter(key="100 Healthy text").first()
    about_award_winning = CommonOption.objects.filter(key="Award Winning text").first()
    spk_title = CommonOption.objects.filter(key="Special Kombo Pack Title").first()
    spk_text = CommonOption.objects.filter(key="Special Kombo Pack Text").first()
    counters = Counter.objects.filter(is_visible=True)
    testimonials = Testimonial.objects.filter(is_visible=True)

    context = {
        'banner_slogan': banner_slogan.value,
        'about_title': about_title.value,
        'about_text': about_text.value,
        'about_image': about_image.photo,
        'about_100_healthy': about_100_healthy.value,
        'about_award_winning': about_award_winning.value,
        'spk_title': spk_title.value,
        'spk_text': spk_text.value,
        'counters': counters,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context=context)
