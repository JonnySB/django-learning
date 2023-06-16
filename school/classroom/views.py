from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, FormView,
                                  CreateView, ListView,
                                  DetailView, UpdateView,
                                  DeleteView)

from classroom.models import Teacher
from classroom.forms import ContactForm

# Template based view!
class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThankYou(TemplateView):
    template_name = 'classroom/thank_you.html'


class TeacherCreateView(CreateView):
    model = Teacher
    # looks for: model_form.html (i.e. teacher_form.html)
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank_you')


class TeacherListView(ListView):
    # looks for: model_list.html (i.e. teacher_list.html)
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'


class TeacherDetailView(DetailView):
    # Return only one model entry (PK) - hence URL needs to be unique
    # looks for: model_detail.html (i.e. teacher_detail.html)
    model = Teacher
    # PK → {{teacher}}


class TeacherUpdateView(UpdateView):
    # will share the model_form.html
    model = Teacher
    # only update first and last name
    fields = ['last_name', 'first_name']
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    # form → Confirm Delete Button
    # Default template name = model_confirm_delete.html
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # Success URL: (note it's a url, not a template file)
    success_url = reverse_lazy('classroom:thank_you')

    # What to do with the form?
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)