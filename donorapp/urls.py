from django.urls import path
from .views import add_donor, update_donor, delete_donor, admin_login

urlpatterns = [
    path("donor/", add_donor),                 # GET & POST
    path("donor/<int:id>/", update_donor),     # PUT
    path("donor/delete/<int:id>/", delete_donor),  # DELETE
    path("admin-login/", admin_login),         # POST
]