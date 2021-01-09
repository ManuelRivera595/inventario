from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"Mi Inventario"})
        
class SamplePageView(TemplateView):
    template_name = "core/sample.html"