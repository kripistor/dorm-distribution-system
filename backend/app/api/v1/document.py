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
    return FileResponse(
        filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
