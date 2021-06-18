from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('', views.main_page, name='Main_page'),
    path('<int:info_id>/', views.inf_detail, name='info_detail'),
    path('exercize/', views.zadan_main, name='Exercize'),
    path('zadan/<int:article_id>/', views.art_detail, name='art_detail'),
    path('photoes/', views.photo_page, name='Photo'),
    path('best/', views.best_works, name='Best'),
    path('info/', views.inf_for, name='Info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
