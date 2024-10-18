from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import FileUploadParser
from rest_framework.viewsets import ModelViewSet

from api.models import ScheduleName
from api.serializers import ScheduleNameSerializer, Response


schema_view = get_schema_view(
   openapi.Info(
      title="JSOON Scheduler",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


class ScheduleViewSet(ModelViewSet):
    """
    A viewset with a separate action to upload files
    """

    queryset = ScheduleName.objects.all()
    serializer_class = ScheduleNameSerializer

    @action(
        detail=True,
        methods=["POST"],
        parser_classes=[FileUploadParser]
    )
    def upload(self, request, **kwargs):
        json_file = self.get_object()

        if "json_file" not in request.data:
            raise ValidationError("There is no file in the HTTP body.")

        file = request.data["json_file"]
        json_file.file.save(file.name, file)
        return Response(ScheduleNameSerializer(json_file).data)
