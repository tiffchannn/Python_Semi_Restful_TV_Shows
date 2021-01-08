from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('shows', views.display_shows), # displays all shows (homepage/root route)
    path('shows/new', views.get_shows_new), # adds new show
    path('shows/post_new', views.post_new), # processes our add new show form
    path('shows/<int:show_id>', views.show_info), # since we're passing in show_id in our url, include show_id in views!
    path('shows/update', views.update),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/destroy', views.delete_show)
]


# delete/<int:show_id>