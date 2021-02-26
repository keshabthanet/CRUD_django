from . import views
from django .urls import path

urlpatterns = [
    path('',views.addview,name='addview'),
    path('delete/<int:id>',views.deleteview,name='deleteview'),
    path('<int:id>/',views.updateview,name='updtaeview'),
]
