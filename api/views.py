from collections import Counter

from rest_framework.decorators import api_view

from rest_framework import serializers
from rest_framework.response import Response


class QuestionSerializer(serializers.Serializer):
    question = serializers.ListField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


@api_view(['POST'])
def lambda_function(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        numbers = serializer.data.get('question')
        ordernado = [num for numbers, c in Counter(numbers).most_common() for num in [numbers] * c]
        resposta = {"solution": ordernado}
        return Response(resposta)

    return Response(serializer.errors)
