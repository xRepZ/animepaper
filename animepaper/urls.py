from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animepic.urls')),
    # path('auth', ),
    path('picture', include('animepic.urls'))
]
