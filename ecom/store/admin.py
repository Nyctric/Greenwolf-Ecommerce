from django.contrib import admin
from .models import Category, Customer, Product, Order, Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# junta la informacion del perfil en la informacion de usuario

class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "last_name", "email"]
    inlines = [ProfileInline]


# dar de baja registro

admin.site.unregister(User)

admin.site.register(User, UserAdmin)