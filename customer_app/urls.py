from django.urls import path

from customer_app import views

urlpatterns = [
    path('customer-home/',views.customer_home,name='customer-home'),
    path('boarding/', views.boarding_view, name='boarding'),
    path('boarding-details/',views.list_boarding_details,name='boarding-details'),
    path('boarding-details-updated/',views.updated_boarding_details,name='boarding-details-updated'),
    path('dog-add/', views.dog_add, name='dog-add'),
    path('dog-view-customer/',views.dog_view_customer,name='dog-view-customer'),
    path('feedback-add/',views.feeds_add,name='feedback-add'),
    path('feeds-view-customer/',views.feeds_view_customer,name='feeds-view-customer'),
    path('staff-view-customer/',views.staff_view_customer,name='staff-view-customer'),
    path('list-reports-customer/',views.list_reports_customer,name='list-reports-customer'),
    path('room-list/',views.room_list,name='room-list'),
    path('view-bill-user', views.view_bill_user, name='view-bill-user'),
    path('pay_bill/<int:id>/', views.pay_bill, name='pay_bill'),
    path('pay_in_direct/<int:id>/', views.pay_in_direct, name='pay_in_direct'),
    path('bill_history', views.bill_history, name='bill_history'),
]