from home.models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission, \
    IsAuthenticated, SAFE_METHODS, DjangoModelPermissions

from rest_framework.response import Response

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    # permission_classes = [DjangoModelPermissions]

class PublisherViewSet(viewsets.ModelViewSet):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = PageNumberPagination


class JournalistViewSet(viewsets.ModelViewSet):

    queryset = Journalist.objects.all()
    serializer_class = JournalistSerializer
    pagination_class = PageNumberPagination


class ManangerViewSet(viewsets.ModelViewSet):

    queryset = Mananger.objects.all()
    serializer_class = ManangerSerializer
    pagination_class = PageNumberPagination

class NationalTViewSet(viewsets.ModelViewSet):

    queryset = NationalT.objects.all()
    serializer_class = NationalTSerializer
    pagination_class = PageNumberPagination



from django.contrib.auth.models import Group
from rest_framework import viewsets
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['POST'])
def load_data_excell(request):
    try:
        import openpyxl
        import io

        file = request.FILES['file']
        wb = openpyxl.Workbook(filename=file)
        wsh = wb.active
        print(wsh['A1'].value)

        return Response('Ok', status=200)
    except Exception as exc:
        return Response(str(exc.with_traceback()), status=200)