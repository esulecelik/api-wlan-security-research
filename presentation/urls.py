from django.urls import path, include

urlpatterns = [
    path("wlan/", include("presentation.uris.wlan_urls")),
]
