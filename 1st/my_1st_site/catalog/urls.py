from django.urls import path
from . import views


app_name = "catalog"

urlpatterns = [
    path('', views.index, name='home_page'),

    path("account/registration_login/", views.registration_loin, name="registration_loin"),
    path("account/logout/", views.logout_user, name="logout"),

    path("id<int:pk>/home/", views.user_home_page, name='user_home_page'),
    path("id<int:pk>/note/add/", views.add_user_content, name='add_user_content'),
    path("id<int:pk>/note/view/<int:note_id>/", views.user_note_detail, name="user_note_detail"),
    path("id<int:pk>/note/<int:note_id>/add_file/", views.add_file_for_note, name='add_file_for_note'),
    path("id<int:pk>/download/<int:file_id>/", views.download_user_file, name='download_user_file'),
    path("id<int:pk>/note/file/<int:file_id>/delete/", views.delete_file_from_note, name='delete_file_from_note'),
    path("id<int:pk>/note/<int:note_id>/delete/", views.delete_user_note, name='delete_user_note'),

    path("test/", views.test_, name="test"),
]