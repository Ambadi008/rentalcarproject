from django.urls import path
from . import views
urlpatterns = [
    path('rentals/',views.sample),
    path('home/',views.home),
    path("cardetails/<int:id>",views.one_item,name="item"),
    path('about/',views.about),
    path('contact/',views.contact),
]

