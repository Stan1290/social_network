from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

class TestPageView(TemplateView):
    template_name = 'test.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'
