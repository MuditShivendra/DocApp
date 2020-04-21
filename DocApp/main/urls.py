from django.urls import path
from main.views import auth, fb_content,views
urlpatterns = [
    path('auth/login/', auth.login, name='login'),
    path('auth/register/', auth.register, name='register'),
    path('', views.HomePage.as_view(), name='home'),
    path('login/',auth.LoginPage.as_view(), name='login'),
    path('dashboard/',views.Dashboard.as_view(), name='dashboard'),
    path('general_public/',views.ListMembersView.as_view(), name='general_public'),
    path('hotspots/',views.HotspotView.as_view(), name='hotspots'),
    path('maps/',views.MapsView.as_view(), name='maps'),
    path('api/highriskplaces', fb_content.get_highriskplaces, name='get-highriskplaces'),
    path('api/profiles/', fb_content.get_all_profile, name='get-profiles'),
    path('api/profiles/<str:id>/', fb_content.get_profile, name='get-profile'),
    path('api/update_status/<str:id>/', fb_content.update_status, name='update-status'),
]

