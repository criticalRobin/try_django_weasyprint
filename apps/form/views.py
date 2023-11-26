from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import ChangeForm
from .forms import ChangeFormForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.template.loader import render_to_string
from weasyprint import HTML


# Create your views here.
def home(request):
    return render(request, "index.html")


class ChangeFormCreateView(CreateView):
    model = ChangeForm
    template_name = "create.html"
    form_class = ChangeFormForm
    success_url = reverse_lazy("form:home")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            user = request.user
            form.user = user
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


def form_pdf(request, pk):
    # Obtener el reporte específico usando la PK
    form = get_object_or_404(ChangeForm, pk=pk)

    # Renderizar la plantilla HTML con los datos
    html_string = render_to_string("form-pdf.html", {"form": form})

    # Generar el PDF
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(presentational_hints=True)

    response = HttpResponse(result, content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename=formulario_{form.pk}.pdf"
    return response
