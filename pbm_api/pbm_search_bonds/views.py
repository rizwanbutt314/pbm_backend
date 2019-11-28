import json

from pbm_bonds.models import (
    BondCategory,
    Bond100,
    Bond200,
    Bond750,
    Bond1500
)
from .serializers import SearchBondSerializer

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import serializers, exceptions
from rest_framework import mixins, generics, filters, status

CATEGORY_MODELS = {
    '100': Bond100,
    '200': Bond200,
    '750': Bond750,
    '1500': Bond1500,
}

"""
data = {
    category: 750,
    date: all | month-day-year(e.g. 11-13-2019),
    searchtype: file(file-id) | range | numbers,
    file: file-id, 
    range: start-value,end-value,
    numbers: comma separated numbers(e.g. 123,1231,454,7565),
}
"""


def generate_filter_query(data):
    searchtype = data['searchtype']

    if searchtype == 'file':
        pass
    elif searchtype == 'range':
        start_value = data['range'].split(',')[0]
        end_value = data['range'].split(',')[1]
        return Q(bond_number__gte=start_value) & Q(bond_number__lte=end_value)
    elif searchtype == 'numbers':
        bond_numbers = data['numbers'].split(',')
        return Q(bond_number__in=bond_numbers)


class BondsSearchAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            request_data = request.data
        except:
            raise exceptions.ValidationError("Invalid JSON: {0}".format(str(e)))

        serializer = SearchBondSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.data

        category_model = CATEGORY_MODELS[serialized_data['category']]
        filter_condition = generate_filter_query(serialized_data)

        queryset = category_model.objects.filter(filter_condition)
        data = list(map(lambda obj: obj.as_dict(), queryset))

        return JsonResponse({'success': True, 'data': data}, status=status.HTTP_200_OK, safe=False)
