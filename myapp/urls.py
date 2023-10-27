from django.urls import path
from myapp.views import reverse_contact_view

urlpatterns = [
    path('', reverse_contact_view, name='reverse_contact_view'),
]
