from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import FileForm
from .models import File


def delete(request, pk):
    if request.method == "POST":
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('list')


class FileListView(ListView):
    model = File
    template_name = 'list.html'
    context_object_name = 'files'


class FileUploadView(CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('list')
    template_name = 'upload.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = timezone.now()
        return super().form_valid(form)
