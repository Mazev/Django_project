from django.urls import path
from test_1.common.views import landing_page

urlpatterns =[
    path('', landing_page),

]