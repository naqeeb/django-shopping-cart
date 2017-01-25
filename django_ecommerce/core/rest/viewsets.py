from rest_framework import viewsets

class BaseViewSet(viewsets.ViewSet):

    def get_queryset(self):
        """ filter qs for current user """
        queryset = super(BaseViewSet, self).get_queryset()
        user = self.request.user
        return queryset.filter(user=user)
