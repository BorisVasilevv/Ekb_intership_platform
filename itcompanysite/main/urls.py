from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('create-news/', views.create_news, name='create_news'),
    path('companies/', include('companies.urls')),
    path('map/', views.map, name='map'),
    path('accounts/', include('accounts.urls')),
    path('internship/', views.internship, name='internship'),
    path('<int:internship_id>/', views.internship_detail, name='internship_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)