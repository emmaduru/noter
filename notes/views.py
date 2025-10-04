from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Note

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        note = self.get_object()
        return note.author == self.request.user

class NoteListView(ListView):
    model = Note
    template_name = "notes/list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["title", "content"]
    template_name = "notes/create.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = "notes/detail.html"
    context_object_name = "note"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
    def post(self, request, *args, **kwargs):
        note = self.get_object()
        if note.author == request.user:
            note.delete()
            return redirect(reverse_lazy("note_list"))
    
class NoteEditView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Note
    fields = ["title", "content"]
    template_name = "notes/edit.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        return reverse_lazy("note_detail", kwargs={"slug": self.object.slug})