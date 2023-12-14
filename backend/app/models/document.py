from typing import Optional, List

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    document_path: Mapped[str] = mapped_column(String, index=True, nullable=False)
