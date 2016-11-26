"""amateur_sports_hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
import clubsec.views as clubsec_views
import leaguepage.views as leaguepage_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', leaguepage_views.index, name='index'),
    url(r'^login/$', leaguepage_views.user_login, name='login'),
    url(r'^logout/$', leaguepage_views.user_login, name='logout'),
    url(r'^club_sec_main/$', clubsec_views.load_club_sec_main,
      name='club_sec_main'),
    # url(r'^register_goal/(?P<host>\d+)/(?P<guest>\d+)$', clubsec_views.register_goal,
    #   name='register_goal'),
    url(r'^submit_goal/$', clubsec_views.register_goal,
       name='submit_goal'),
    url(r'^submit_goal/(?P<score_host>\d+)/(?P<score_guest>\d+)/(?P<scorer_host>\w+)/(?P<scorer_guest>\w+)$', clubsec_views.register_goal,
       name='submit_goal'),
]
