from django.urls import path
from . import views
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete, ReportePDF, ReporteExcel, BuscarView

pages_patterns =([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
    path('reporte_pdf/',ReportePDF.as_view(), name="reporte_pdf"),
    path('reporte_excel/',ReporteExcel.as_view(), name="reporte_excel"),
    path('buscar/',BuscarView.as_view(), name="buscar"),
], 'pages')