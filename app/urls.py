from django.urls import path
from . import views

urlpatterns = [
    path('', views.etusivu, name='etusivu'),
    path('kirjat/', views.kirjalistview, name='kirjalist'),
    path('addkirja/', views.addkirja, name='addkirja'),
    path('deletekirja/<int:id>/', views.deletekirja, name='deletekirja'),
    path('login/', views.loginview, name='login'),
    path('login_action/', views.login_action, name='login_action'),
    path('logout/', views.logout_action, name='logout'),
    path('edit_kirja/<int:id>/', views.edit_kirja_get, name='edit_kirja_get'),
    path('edit_kirja_post/<int:id>/', views.edit_kirja_post, name='edit_kirja_post'),
    path('lainat/', views.lainalistview, name='lainalist'),
    path('addlaina/', views.addlaina, name='addlaina'),
    path('update_laina/<int:id>/', views.update_laina_status, name='update_laina'),
]