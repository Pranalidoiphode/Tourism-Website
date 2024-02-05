"""
URL configuration for tourismproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tourismapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('explore/',views.explore,name="explore"),
    path('rajhasthan/',views.rajhasthan,name="rajhasthan"),
    path('kerala/',views.kerala,name="kerala"),
    path('goa/',views.goa,name="goa"),
    path('taj/',views.taj,name="taj"),
    path('andaman/',views.andaman,name="andaman"),
    path('hampi/',views.hampi,name="hampi"),
    path('coorg/',views.coorg,name="coorg"),
    path('himachal/',views.himachal,name="himachal"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path('register/',views.register,name="register"),
    path('add_to_book/<int:t_id>',views.add_to_book,name="add_to_book"),
    path("book/", views.book, name="book"),
    path("remove_from_book/<int:t_id>", views.remove_from_book,name="remove_from_book"),
    path('orders/',views.orders,name='orders'),
    path("updatepeople/<qv>/<t_id>", views.updatepeople, name="updatepeople"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path("dateselect/", views.dateselect, name="dateselect"),
    path('makepayment/',views.makepayment,name='makepayment'),
    path('showorders/',views.showorders,name='showorders'),
    # path("get_date_from_id/<t_id>", views.get_date_from_id, name="get_date_from_id"),
    # path('increase/', views.increase_quantity, name='increase_quantity'),
    # path('decrease/', views.decrease_quantity, name='decrease_quantity'),
    

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
