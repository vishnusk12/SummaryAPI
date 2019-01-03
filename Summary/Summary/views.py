'''
Created on 19-Dec-2018

@author: Vishnu
'''

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .model import Summary

@permission_classes((permissions.AllowAny,))
class Recognition(viewsets.ViewSet):
    def create(self, request):
        question = request.data
        response = Summary(question['url'], question['number'])
        return Response(response)