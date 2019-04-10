from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from passporteye import read_mrz
from rest_framework import parsers
from rest_framework import status

class FileUploadView(APIView):
    # parser_classes = (parsers.MultiPartParser, )

    def post(self, request):
        img_url = request.data["img_url"]
        print('Image url', img_url)
        up_file = 'https://firebasestorage.googleapis.com/v0/b/kycapp-18ab0.appspot.com/o/id2.jpg?alt=media&token=623a27e4-d508-4024-b360-bc2126c5120d'
        # up_file = request.FILES['myfile']
        print('Faili', up_file)
        mrz = read_mrz(up_file)
        pass_data = mrz.to_dict()
        print("Mrz fILE",pass_data["optional2"])
        # destination = open('/Users/Username/' + up_file.name, 'wb+')
        # for chunk in up_file.chunks():
        #     destination.write(chunk)
        #     destination.close()
        # ...
        # do some stuff with uploaded file
        # ...
        # return Response(mrz, status.HTTP_201_CREATED)
