# MarketHub

## Backend setup

1. Copy `.env.example` to `.env` and replace the development placeholders.
2. From the project root, start PostgreSQL:

   ```powershell
   docker compose up -d db
   ```

   PostgreSQL is available locally on port `5434`. Redis is not included in the stack yet.

3. Install the backend dependencies and apply database migrations:

   ```powershell
   Set-Location backend
   poetry install
   poetry run alembic upgrade head
   ```

4. Start the API:

   ```powershell
   poetry run uvicorn backend.main:app --reload
   ```
