import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic

from application.models import Order


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(employee=self.request.user)


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Order

    def post(self, request, *args, **kwargs):
        if request.POST.get("confirm_delete") == "True":
            order = self.get_object()
            time = datetime.datetime.now()
            employee = order.employee
            context = {
                "id": order.id,
                "task_id": order.task_id,
                "name": order.name,
                "employee": f"{employee.first_name} ({employee.position})",
                "time": time,
            }
            order.delete()

            return render(
                request,
                "application/order_delete_info.html",
                context
            )

        return redirect("order-list")


class ConfirmationView(LoginRequiredMixin, generic.TemplateView):
    template_name = "application/order_delete_info.html"
