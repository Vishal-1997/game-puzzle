# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from list.models import Game
from list.serializers import GameSerializer


@api_view(['GET'])
def game_view(request):
    queryset = Game.objects.all()
    return Response(status=200, data=GameSerializer(queryset, many=True).data)


@api_view(['GET'])
def game_view_id_filter(request, id):
    queryset = Game.objects.filter(pk=id)
    return Response(status=200, data=GameSerializer(queryset, many=True).data)


@api_view(['POST'])
def game_view_title_filter(request, title):
    queryset = Game.objects.filter(title=title)
    return Response(status=200, data=GameSerializer(queryset, many=True).data)



