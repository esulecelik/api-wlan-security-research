from ..views.wlan_view import DeauthAttackView
from django.urls import path,include

urlpatterns = [
    path("deauth/", DeauthAttackView.as_view(), name="wlan-deauth-attack"),
]