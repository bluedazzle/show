from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from core.models import Host


class IndexView(DetailView):
    template_name = 'index.html'
    model = Host

    def get_object(self, queryset=None):
        host = self.request.META.get('HTTP_HOST')
        try:
            host = self.model.objects.get(host=host)
            return host
        except Exception as e:
            return None
