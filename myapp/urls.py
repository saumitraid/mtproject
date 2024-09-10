from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home-page'),
    path('about', views.about, name='about-page'),
    path('stdreg', views.stdreg, name='stdreg-page'),
    path('stdview', views.viewStd, name='stdview-page'),
    path('stddel/<int:sid>', views.delStd, name='stddel-page'),
    path('stdupd/<int:sid>', views.updStd, name='stdupd-page'),
    path('prddetails/<int:pid>', views.prdDetails, name='pdetails-page'),
    path('cateDetails/<int:catid>', views.cateDetails, name='cat-details-pg'),
    path('user-reg', views.userReg, name='user-reg'),
    path('user-log', views.userLogin, name='user-log'),
    path('user-logout', views.userLogout, name='user-logout'),
]

