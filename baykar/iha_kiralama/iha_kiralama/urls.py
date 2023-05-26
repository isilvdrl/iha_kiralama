
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIha, name="showIha" ),
    path('Insert', views.insertIha, name="insertIha" ),
    path('Edit/<int:id>', views.editIha, name="editIha" ),
    path('Update/<int:id>', views.updateIha, name="updateIha" ),
    path('Delete/<int:id>', views.deleteIha, name="deleteIha" ),
    path('Login/', views.loginView, name='loginView'),
    path('Register/', views.registerIha, name="registerIha" ),
]
