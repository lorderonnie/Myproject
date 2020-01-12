from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name='home'),
    path('project/profile/',views.profile,name="profile"),
    url(r'^updateprofile/$',views.updateprofile,name='updateprofile'),
    url(r'^newpost/',views.newpost,name='newpost'),
    path('logout/',views.logout,name = 'logout'),
    path('review/new/<int:id>/',views.review,name='review'),
    path('review/view/<int:id>/',views.review_view,name='view'),  
    path('search/',views.search_results,name='search'),
    path('review/project/<int:id>',views.post_review, name='post-review'),
    path('rate/post/<int:id>',views.post_rate, name='post-rate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

