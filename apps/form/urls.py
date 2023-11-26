from django.urls import path
from . import views

app_name = "form"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.ChangeFormCreateView.as_view(), name="create"),
    path("export/<int:pk>/", views.form_pdf, name="pdf"),
]
