from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from recipes import views
from recipes.urls import ingredientUrls, urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/recipes/', include(urlpatterns)),
    path('api/ingredients/', include(ingredientUrls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
