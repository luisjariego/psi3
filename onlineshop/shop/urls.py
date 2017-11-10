# New urls for our app

from django.conf.urls import url
from shop import views
from django.conf.urls import static 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^index/', views.index, name='index'), #Index
    #url(r'^about/', views.about, name='about'), # About
    #url(r'^base/', views.base, name='base'), # Base
    #url(r'^add_category/$', views.add_category, name='add_category'), #Category (add)
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', #Category (show)
    #views.show_category, name='show_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_product/$', views.add_product, name='add_product'), #Page (add)
    url(r'^$', views.index, name='product_list'),
    url(r'^(?P<catSlug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<prodSlug>[-\w]+)/$', views.product_detail, name='product_detail'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
