class ActionBasedSerializerModelViewSetMixin:
    """
    A :py:class:`rest_framework.viewsets.ModelViewSet` mixin that allows configuring a per-action serializer.

    To make use of this mixin one needs to inherit from it and populate the `action_serializer_class`attribute.
    If no serializer class can be found for an action, the default :py:attr:`serializer_class` is used.

    Example configuration: `action_serializer_class = {'list': MySerializer}`.
    """

    def get_serializer_class(self):
        try:
            return self.action_serializer_class[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
