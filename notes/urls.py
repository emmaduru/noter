from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.NoteCreateView.as_view(), name="note_create"),
    path("<slug:slug>/edit/", views.NoteEditView.as_view(), name="note_edit"),
    path("<slug:slug>/", views.NoteDetailView.as_view(), name="note_detail"),
    path("", views.NoteListView.as_view(), name="note_list")
]