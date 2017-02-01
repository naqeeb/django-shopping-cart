from rest_framework import viewsets

class BaseViewSet(viewsets.ViewSet):
    serializers = {
        'default': None
    }

    def get_serializer_class(self):
        """ return the correct serialzer per action """
        return self.serializers.get(self.action,
                        self.serializers['default'])

    def get_queryset(self):
        """ filter qs for current user """
        queryset = super(BaseViewSet, self).get_queryset()
        user = self.request.user
        return queryset.filter(user=user)
