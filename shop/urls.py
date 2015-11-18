from django.conf.urls import patterns, include, url

from shop import views

urlpatterns = [
    url(r'^$', views.catalog, name='catalog'),
    url(r'^search$', views.search_item, name='search_item'),
    url(r'^catalog/(?P<category_id>\d+)?$', views.catalog, name='catalog'),
    url(r'^catalog/(?P<category_id>\d+)/(?P<item_id>\d+)$', views.item, name='item'),
    url(r'^signin$', views.LoginFormView.as_view(), name='signin'),
    url(r'^signup$', views.RegisterFormView.as_view(), name='signup'),
    url(r'^logout', views.LogoutView.as_view(), name='logout'),
    url(r'^userpage', views.userpage, name='userpage'),
    url(r'^cart', views.cart, name='cart'),
    url(r'^order', views.order, name='order'),
    url(r'^bugreport', views.bugreport, name='bugreport'),
    #url(r'^adm', views.adm, name='adm'),
]