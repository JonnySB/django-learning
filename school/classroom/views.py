from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from classroom.forms import ContactForm

# Template based view!
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # Success URL: (note it's a url, not a template file)
    success_url = reverse_lazy('classroom:thank_you')

    # What to do with the form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)