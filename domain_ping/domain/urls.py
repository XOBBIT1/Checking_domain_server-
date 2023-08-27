from django.urls import path

from .api.views.domain import (
    DomainGetAllViews,
    DomainPutViews,
    DomainDeleteViews,
    DomainPostViews,
    DomainRetrieveView,
)

urlpatterns = [
    path('domain/get_all/', DomainGetAllViews.as_view(), name='domain-list'),
    path('domain/create/', DomainPostViews.as_view(), name='domain-post'),
    path('domain/get/<int:id>/', DomainRetrieveView.as_view(), name='domain-one'),
    path('domain/put/<int:id>/', DomainPutViews.as_view(), name='domain-put'),
    path('domain/delete/<int:id>/', DomainDeleteViews.as_view(), name='domain-delete'),
]
