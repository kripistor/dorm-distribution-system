from fastapi import APIRouter, UploadFile, File
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.schemas.document import FileInfo
from app.schemas.media_file import AppMediaFileCreate
from app.utils import S3Client

router = APIRouter(prefix="/documents")


@router.post(
    "/upload",
    response_model=FileInfo,
    status_code=200,
    response_description="Upload a file",
)
async def upload_file(
        session: CurrentAsyncSession,
        file_info: AppMediaFileCreate,
        response: Response,
        file: UploadFile = File(...),
):
    filename = (
        f"uploads/{file_info.section_id}/{file_info.short_tag}-{file_info.filename}"
    )
    s3 = S3Client()
    resp = await s3.upload_object_to_s3(file.file, filename)
    return resp
