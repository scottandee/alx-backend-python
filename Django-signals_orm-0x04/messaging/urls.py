from messaging import views
from django.urls import path, include


urlpatterns = [
    path('users/', view=views.delete_user),
    path('messages/', view=views.fetch_messages)
]
