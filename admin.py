from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from list.models import Game
from list.resources import GameResource


class GameAdmin(ImportExportModelAdmin):

    resource_class = GameResource


admin.site.register(Game, GameAdmin)
