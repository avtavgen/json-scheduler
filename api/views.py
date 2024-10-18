import json

from ninja import NinjaAPI, File
from ninja.errors import ValidationError
from ninja.files import UploadedFile
from ninja.responses import Response

from api.auth import AuthBearer
from api.serializers import Root

api = NinjaAPI()


@api.post("/upload", response=Root)
def upload(request, file: UploadedFile = File(...)):
    try:
        data = file.read().decode('utf8').replace("'", '"')
        data = json.loads(data)
        json_root = Root(**data)
    except (ValueError, ValidationError) as e:
        return Response(status_code=404, data={"message": str(e)})
    return json_root


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}
