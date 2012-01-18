from django.contrib import admin

from games.core.models import Game, Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_key', 'user')
    exclude = ('api_key',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('client', 'name')
    list_filter = ('client',)
    ordering = ('client', 'name')

admin.site.register(Client, ClientAdmin)
admin.site.register(Game, GameAdmin)
