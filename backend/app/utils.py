import logging

import aioboto3
from aioboto3 import Session

from app.core.config import settings
from app.schemas.document import FileInfo

logger = logging.getLogger(__name__)


class S3Client:
    def __init__(self, bucket_name: str = settings.S3_BUCKET_NAME):
        self.bucket_name = bucket_name
        self.aws_access_key_id = settings.S3_ACCESS_KEY_ID
        self.aws_secret_access_key = settings.S3_SECRET_ACCESS_KEY
        self.aws_endpoint_url = settings.S3_ENDPOINT_URL

    async def _create_session(self) -> Session:
        logger.info("Creating S3 session.")
        logger.info(f"Id: {self.aws_access_key_id}")
        logger.info(f"Secret: {self.aws_secret_access_key}")
        session = aioboto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )
        client = session.client("s3", endpoint_url=self.aws_endpoint_url)
        return client

    async def upload_object_to_s3(self, content, file_name: str) -> FileInfo | None:
        client = await self._create_session()
        async with client as s3:
            resp = await s3.put_object(
                Body=content, Bucket=self.bucket_name, Key=file_name
            )
            if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                logger.info(f"File {file_name} uploaded successfully.")
                return FileInfo(
                    filename=file_name,
                )
            else:
                logger.error(f"Failed to upload file {file_name}.")
                return None
