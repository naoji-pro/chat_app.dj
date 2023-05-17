from django.contrib import admin
from django.urls import path
from chat.views import frontpage,chatpage,back_to_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage),
    path('<slug:slug>/',chatpage,name="chatpage"),
    path('',back_to_page,name="back_to_page")
]
