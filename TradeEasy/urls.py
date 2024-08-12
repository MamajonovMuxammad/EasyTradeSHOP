from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('orders/', include('orders.urls', namespace='orders')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)