from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/',login, name='login'),
    path('plataforma',plataforma, name='plataforma'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil',perfil, name='perfil'),
    path('usuariocadastrado',usuario_cadastrado,name='usuariocadastrado'),
    path('detalhe/<int:id>',detalhe, name='detalhe'),
    path('mercado/', mercado, name="mercado"),
    path('produto/', produto, name="produto"),
    path('delivery/', delivery, name="delivery"),
    path('noticias/', noticias, name="noticia"),
    path('sobrenos/', sobrenos, name="sobrenos"),
    path('detalhe_produto/<int:id>', detalhe_produto, name="detalhe_produto"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('resetarsenha/', resetarsenha, name="resetarsenha"),
    path('loja/<int:id>', loja, name="loja"),
    path('carrinho/', Carrinho, name="carrinho"),
    path('delete/<int:id>', delete, name="delete")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)