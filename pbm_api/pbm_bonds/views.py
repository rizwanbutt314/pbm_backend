from .models import BondCategory
from .serializers import BondCategorySerializer
from rest_framework import mixins, generics, filters, status


class APIIndex(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    serializer_class = BondCategorySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('category',)

    def get_queryset(self):
        return BondCategory.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
