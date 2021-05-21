from rest_framework import status
from rest_framework.response import Response
from .models import DealData
from collections import OrderedDict


def pars_data(data):
    data = data.replace("\r", "").split('\n')
    if data == ['']:
        return Response(status=status.HTTP_409_CONFLICT, data='File is empty')

    result = {}

    for row in data[1:]:
        try:
            row = row.split(',')
            if row == ['']:continue
            name = row[0]
            count_sum = int(row[2]) * int(row[3])
            gems = row[1]
            if name not in result:
                result[name] = {'count_sum': count_sum, 'gems': [gems, ]}
            else:
                result[name]['count_sum'] += count_sum
                result[name]['gems'].append(gems)
        except ValueError:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'Invalid data type'})

    result = OrderedDict(sorted(result.items(), key=lambda x: x[1]['count_sum'], reverse=True))

    write_db(result)

    return Response(status=status.HTTP_201_CREATED, data={'message': 'File uploaded successfully'})


def write_db(data):
    DealData.objects.all().delete()

    for num_iter, (key, value) in enumerate(data.items()):
        DealData.objects.create(
            username=key,
            spent_money=value['count_sum'],
            gems=check_gems(data, num_iter, value['gems'])
        )
        if num_iter == 4:
            break


def check_gems(data, num_iter, gems_user):
    others_gems_user = []

    for num, (key, value) in enumerate(data.items()):
        if num == 5:
            break
        if num == num_iter:
            continue
        others_gems_user.extend(value['gems'])

    result_gems = set(gem for gem in gems_user if gem in others_gems_user)

    return result_gems
