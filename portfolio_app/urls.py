from django.urls import path,include
from portfolio_app import views


app_name= 'portfolio_app'


urlpatterns = [
    path('',views.index,name='index'),
    # path('education/',views.education,name='education'),
    # path('projects/',views.projects,name='projects'),
    # path('skills/',views.skills,name='skills'),
    # path('interests/',views.interests,name='interests'),
    

]
