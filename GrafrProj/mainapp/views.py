from django.views.generic import ListView, DetailView, CreateView
from .models import TelegrafModel
from .forms import TelegrafForm


# make Forbidden 403 - LoginRequiredMixin ?
class List(ListView):
    model = TelegrafModel
    template_name = 'mainapp/list.html'
    context_object_name = 'obj'
    # allow_empty = False # objects.filter() returns empty QuerySet when no match found, we can use "allow_empty" to show HTTP404

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все записи'
        return context

    def get_queryset(self):
        return TelegrafModel.objects.all()


class Pub(DetailView):
    model = TelegrafModel
    template_name = 'mainapp/pub.html'
    context_object_name = 'obj'
    pk_url_kwarg = 'uri'  # otherwise need <pk:uri> or <slug:uri> in route

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TelegrafModel.objects.get(uri=self.kwargs['uri'])
        return context

    def get_queryset(self):
        return TelegrafModel.objects.filter(uri=self.kwargs['uri'])


class Add(CreateView):
    form_class = TelegrafForm
    template_name = 'mainapp/add.html'
    # success_url = reverse_lazy('add')
