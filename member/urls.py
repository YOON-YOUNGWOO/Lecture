from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/',views.login, name='login'),
    path('login_check/',views.login_check, name='login_check'),
    path('signup/',views.signup, name='signup'),
    path('signupcheck/',views.signupcheck, name='signupcheck'),
    path('logout/',views.logout, name='logout'),
    path('editinfo/',views.editinfo, name='editinfo'),
    path('profile/',views.profile, name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('memberleave/', views.memberleave, name='memberleave'),
    path('product/',views.product, name='product'),
    path('id_ck/', views.id_ck, name="id_ck"),
    path('class_plus/',views.class_plus, name="class_plus"),
    path('upload_file/',views.upload_file, name="upload_file"),
    path('test/',views.test, name="test"),
    path('test2/',views.test2, name="test2"),
    path('ck_box/', views.ck_box, name="ck_box"),
    path('ck_box2/', views.ck_box2, name="ck_box2"),
    path('delete_lecture/',views.delete_lecture, name="delete_lecture"),
    path('lecture_add/',views.lecture_add, name="lecture_add")
]
