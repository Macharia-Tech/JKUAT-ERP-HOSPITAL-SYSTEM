from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('viewdoc/', views.view_doctor, name='view-doctor'),
    path('addoc/', views.Add_doctor.as_view(), name='add-doctor'),
    path('editdoc/<int:id>/', views.Update_doctor.as_view(), name='update-doctor'),
    path('deldoc/<int:id>/', views.delete_doctor, name='delete-doctor'),
    path('addpnt/', views.Add_patient.as_view(), name='add-patient'),
    path('editpnt/<int:id>/', views.Update_patient.as_view(), name='update-patient'),
    path('delpnt/<int:id>/', views.delete_patient, name='delete-patient'),
    path('viewpnt/', views.view_patient, name='view-patient'),
    path('addmed/', views.Add_medicine.as_view(), name='add-medicine'),
    path('editmed/<int:id>/', views.Update_medicine.as_view(), name='update-medicine'),
    path('delmed/<int:id>/', views.delete_medicine, name='delete-medicine'),
    path('viewmed/', views.view_medicine, name='view-medicine'),
    path('log/', views.log,name="log"),
    path('logot/', views.log_out,name="logout"),
]