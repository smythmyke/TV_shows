from django.urls import path
from . import views

urlpatterns = [
    #renders page with create form
    path('', views.index),
    #show specific show info
    path('shows/<int:show_id>', views.profile),
    #edit specific show
    path('shows/<int:show_id>/edit', views.edit),
    #render the page to create a show
    path('shows/create', views.create),
    #delete a show
    path('shows/<int:show_id>/delete', views.delete),
    #update information submitted
    path('shows/<int:show_id>/update', views.update),
    path('shows/deleted', views.deleted),
    path('shows/all_shows', views.all_shows)
    
]