from django.contrib import admin

# Register your models here.
from .models import User, UserOtp, Transaction


class UserSearch(admin.ModelAdmin):
    search_fields = ['name', 'phone', 'username']


class TransactionSearch(admin.ModelAdmin):
    search_fields = ['user', 'date_of_transaction', 'trans_id']


admin.site.register(User, UserSearch)
admin.site.register(UserOtp)
admin.site.register(Transaction, TransactionSearch)
