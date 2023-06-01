from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *
from django.contrib.auth import get_user_model
# Create your views here.


class CreateUserView(generics.GenericAPIView):
    serializer_class = CreateUserSerializers

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUser(generics.GenericAPIView):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = User.objects.get(uid=user.uid)
        serializer = self.serializer_class(instance=data)

        return Response(data=serializer.data)


class UserStacks(generics.GenericAPIView):
    serializer_class = UserJobStackSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        stack = request.data

        serializer = self.serializer_class(data=stack)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        user_stacks = UserStack.objects.filter(user_id=user.uid, many=True)
        serializer = self.serializer_class(instance=user_stacks)

        return Response(data=serializer.data)

    def delete(self, request, id):
        user_stack = get_object_or_404(UserStack, pk=id)
        user_stack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
