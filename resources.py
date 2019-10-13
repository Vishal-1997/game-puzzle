from import_export import resources

from list.models import Game


class GameResource(resources.ModelResource):
    class Meta:
        model = Game
