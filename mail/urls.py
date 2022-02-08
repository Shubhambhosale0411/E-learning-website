from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('aboutus/',views.index2,name="index2"),
    path('contact_us/',views.index3,name="index3"),
    path('service_accounting/',views.index4,name="index4"),
    path('service_bpo/',views.index5,name="index5"),
    path('service_business_setup/',views.index6,name="index6"),
    path('service_financial_coaching/',views.index7,name="index7"),
    path('service_investment_opportunities/',views.index8,name="index8"),
    path('service_property_management/',views.index9,name="index9"),
    path('service_tax_management/',views.index10,name="index10"),

    path('test/',views.test,name="test"),
    path('send/',views.createMail,name="createMail"),
    path('save_user/',views.saveUser,name="saveUser"),
    #new
    path('export_to_csv',views.export_to_csv,name="export_to_csv")
    #path('download-csv/',views.contact_download,name="contact_download"),
]
