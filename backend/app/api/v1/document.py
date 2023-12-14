from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from app.deps.db import CurrentAsyncSession
from app.repo.document_repo import DocumentRepo

router = APIRouter(prefix="/documents")


@router.get("/generate_report")
async def generate_report(session: CurrentAsyncSession):
    document_repo: DocumentRepo = DocumentRepo(session)
    filename = await document_repo.generate_report()
    return FileResponse(filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        headers={"Content-Disposition": f"attachment; filename={filename}"})

# @router.post(
#    "/upload",
#    response_model=FileInfo,
#    status_code=200,
#    response_description="Upload a file",
# )
# async def upload_file(
#        session: CurrentAsyncSession,
#        file_info: AppMediaFileCreate,
#        response: Response,
#        file: UploadFile = File(...),
# ):
#    filename = (
#        f"uploads/{file_info.section_id}/{file_info.short_tag}-{file_info.filename}"
#    )
#    s3 = S3Client()
#    resp = await s3.upload_object_to_s3(file.file, filename)
#    return resp
