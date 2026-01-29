from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import ExpenseSerializer
class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        queryset = Expense.objects.all()
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')

        if category:
            queryset = queryset.filter(category=category)
        if date:
            queryset = queryset.filter(date=date)

        return queryset

