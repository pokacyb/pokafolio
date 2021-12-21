from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog'),
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
]
