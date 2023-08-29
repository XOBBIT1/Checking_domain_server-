from datetime import datetime

from rest_framework import views, status, generics, mixins
from rest_framework.response import Response

from ..serializers.domain import DomainSerializer
from ...models import Domain


class DomainGetAllViews(views.APIView):

    def get(self, request):
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)


class ChartView(views.APIView):
    def get(self, request):
        domains = Domain.objects.all()
        chart_data = []

        for domain in domains:
            chart_data.append({
                "domain_name": domain.domain_name,
                "ping_of_domain": [
                    {"hour": datetime.now().hour, "ping": int(domain.ping_of_domain)}
                ]
            })

        return Response(chart_data)


class DomainRetrieveView(generics.RetrieveAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    lookup_field = 'id'


class DomainPostViews(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Domain.objects.filter(domain_name__gt=10)
    serializer_class = DomainSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DomainPutViews(views.APIView):
    serializer_class = DomainSerializer

    def put(self, request, id):
        try:
            domain = Domain.objects.get(pk=id)
        except Domain.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(domain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DomainDeleteViews(views.APIView):
    def delete(self, request, id):
        try:
            domain = Domain.objects.get(pk=id)
        except Domain.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        domain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
