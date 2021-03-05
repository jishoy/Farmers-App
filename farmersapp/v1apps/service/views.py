from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,\
    RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Service
from .serializers import ServiceSerializer


class ServiceAddAPIView(CreateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)


class ServiceHistoryListView(ListAPIView):
    permission_classes = ()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.filter(user=self.kwargs.get('user_id'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({"status": "false"}, status=status.HTTP_204_NO_CONTENT)
        else:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({"data": serializer.data, "status": "true"}, status=status.HTTP_200_OK)

