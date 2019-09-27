from .models import BondCategory, BondDrawDates
from .serializers import BondCategorySerializer, BondDrawDatesSerializer
from rest_framework import mixins, generics, filters, status


class BondCategoryAPIIndex(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    serializer_class = BondCategorySerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('category',)

    def get_queryset(self):
        return BondCategory.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BondDrawDatesAPIIndex(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    serializer_class = BondDrawDatesSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('year', 'date',)

    def get_queryset(self):
        category = self.kwargs.get('category')
        try:
            return BondCategory.objects.get(category=category).bonddrawdates_set
        except BondCategory.DoesNotExist:
            return BondCategory.objects.none()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
