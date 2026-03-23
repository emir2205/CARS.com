from django.views import generic


class TourismHomeView(generic.TemplateView):
    template_name = 'tourism.html'
