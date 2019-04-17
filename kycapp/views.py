from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from passporteye import read_mrz
from django.http import HttpResponse, JsonResponse
from rest_framework import parsers
from rest_framework import status
import json
from . import serializers

class FileUploadView(APIView):
    # parser_classes = (parsers.MultiPartParser, )

    def post(self, request):
        #up_file = 'https://firebasestorage.googleapis.com/v0/b/kycapp-18ab0.appspot.com/o/dfc195e4-9eed-44de-973f-4a2b03d8ec4f1825852140.jpg?alt=media&token=98e7f9f3-84c8-41a1-a277-ad55375121f6'
        up_file = request.data['myfile']
        print('Faili', up_file)
        mrz = read_mrz(up_file)
        pass_data = mrz.to_dict()
        mrz_data = {}
        mrz_data["surname"] = pass_data["surname"]
        mrz_data["sex"] = pass_data["sex"]
        mrz_data["date_of_birth"] = pass_data["date_of_birth"]
        mrz_data["optional2"] = pass_data["optional2"]
        print("Mrz fILE",pass_data["optional2"])
        serializer = serializers.MrzSerializers(data=mrz_data)
        serializer.is_valid()
        # destination = open('/Users/Username/' + up_file.name, 'wb+')
        # for chunk in up_file.chunks():
        #     destination.write(chunk)
        #     destination.close()
        # ...
        # do some stuff with uploaded file
        # ...
        # json_data = json.dumps(pass_data)
        return JsonResponse(serializer.data, safe=False, status=200)
