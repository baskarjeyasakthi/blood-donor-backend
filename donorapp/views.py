from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DonorSerializer
from .models import Donor
from django.contrib.auth import authenticate
from rest_framework import status


@api_view(['GET', 'POST'])
def add_donor(request):

    if request.method == 'GET':
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)

    serializer = DonorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['PUT'])
def update_donor(request, id):
    try:
        donor = Donor.objects.get(id=id)
    except Donor.DoesNotExist:
        return Response({"error": "Donor not found"}, status=404)

    serializer = DonorSerializer(donor, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_donor(request, id):
    try:
        donor = Donor.objects.get(id=id)
        donor.delete()
        return Response({"message": "Deleted Successfully"})
    except Donor.DoesNotExist:
        return Response({"error": "Donor not found"}, status=404)


@api_view(['POST'])
def admin_login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None and user.is_superuser:
        return Response(
            {"message": "Login Successful"},
            status=status.HTTP_200_OK
        )

    return Response(
        {"error": "Invalid username or password"},
        status=status.HTTP_401_UNAUTHORIZED
    )