from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from apps.forms import PersonForm
from apps.models import Person, Job


class HomeView(ListView):
    model = Person
    template_name = 'contacts.html'


class HomeAdd(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobs'] = Job.objects.all()
        return context


class HomeDeleteView(DeleteView):
    model = Person
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class HomeUpdateView(UpdateView):
    model = Person
    template_name = 'update.html'
    fields = ('fullname', 'email', 'address', 'phone')
    # form_class = PersonForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
