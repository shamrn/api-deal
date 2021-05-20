from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DealData
from .serializers import FileCsvSerialiser
from .pars import pars_data


@api_view(['GET', 'POST'])
def get_deal(request):
    if request.method == 'GET':
        deals = DealData.objects.all()
        serializer = FileCsvSerialiser(deals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        key = list(request.FILES)[0]
        file = request.FILES[key]

        if 'csv' not in str(file):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'Valid format.csv'})
        else:
            data = file.read().decode('utf-8')
            return pars_data(data)
