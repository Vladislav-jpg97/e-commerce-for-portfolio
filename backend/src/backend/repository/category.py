from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.models import Category, CategoryTranslation
from backend.repository.base import BaseRepository
from backend.repository.mixins import (
    AddRepositoryMixin,
    UpdateRepositoryMixin,
    DeleteRepositoryMixin,
    RetrieveRepositoryMixin,
    ListRepositoryMixin,
    PaginatedListRepositoryMixin
)


class CategoryRepository(
    AddRepositoryMixin[Category],
    RetrieveRepositoryMixin[Category],
    UpdateRepositoryMixin[Category],
    DeleteRepositoryMixin[Category],
    ListRepositoryMixin[Category],
    PaginatedListRepositoryMixin[Category],
    BaseRepository
):
    model = Category
    base_query = select(Category).options(
        selectinload(Category.translations)
    )

    async def get_by_slug(self, slug: str) -> Category | None:
        stmt = self.base_query.where(
            Category.translations.any(CategoryTranslation.slug == slug)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
