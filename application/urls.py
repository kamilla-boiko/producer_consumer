from django.urls import path

from application.views import OrderListView, OrderDeleteView, ConfirmationView

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order-list"),
    path(
        "orders/<int:pk>/delete/",
        OrderDeleteView.as_view(),
        name="order-delete"
    ),
    path(
        "orders/deleted/",
        ConfirmationView.as_view(),
        name="order-confirm-delete"
    ),
]


app_name = "application"
