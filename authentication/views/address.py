from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from authentication.serializers.address import AddressSerializer
from authentication.models import Address
from utils.response import APIResponse

class AddressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = Address.objects.filter(user=request.user)
        serializer = AddressSerializer(addresses, many=True)
        return APIResponse.success(serializer.data)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return APIResponse.success(serializer.data, "Address created")
