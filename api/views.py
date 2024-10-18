import json

from ninja import NinjaAPI, File
from ninja.files import UploadedFile

from api.auth import AuthBearer
from api.serializers import Root

api = NinjaAPI()


@api.post("/upload", response=Root)
def upload(request, file: UploadedFile = File(...)):
    data = file.read().decode('utf8').replace("'", '"')
    data = json.loads(data)
    json_root = Root(**data)
    return json_root


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}
