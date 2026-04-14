# Gemini Project Configuration

This file contains foundational mandates and project-specific instructions for Gemini CLI. These instructions take precedence over general defaults.

## Project Rules & Mandates

### Git Conventions
- **Conventional Commits:** Use the following format for all commit messages:
  - `feat: description` - New features
  - `fix: description` - Bug fixes
  - `perf: description` - Performance improvements
  - `deps: description` - Dependency updates
  - `docs: description` - Documentation changes
  - `ci: description` - CI/CD changes
  - `chore: description` - Other changes
- **No AI Attribution:** Never include "Co-Authored-By: Gemini" or similar AI attribution lines in commits.

### Engineering Standards
- **Database Migrations:** Always use `flask db migrate -m "description"` and `flask db upgrade` when modifying models in `app/models.py`.
- **Testing:** Verify changes locally by running the application or relevant test suites before finalizing.

---

## Project Overview

Willman is a self-hosted vehicle management application built with Flask. It tracks fuel consumption, expenses, maintenance, trips, EV charging, and more.

### Tech Stack
- **Backend:** Flask (Python 3.12)
- **Database:** SQLite with SQLAlchemy ORM (stored at `/data/willman.db`)
- **Frontend:** Jinja2 templates with Bootstrap 5.3 and jQuery
- **Charts:** Chart.js
- **PDF Generation:** WeasyPrint
- **Production Server:** Gunicorn
- **Deployment:** Docker (Port 5151)

### Project Structure
- `app/`: Core application logic
  - `models.py`: SQLAlchemy models (User, Vehicle, FuelLog, etc.)
  - `routes/`: Blueprint route handlers (auth, vehicles, fuel, etc.)
  - `services/`: Business logic (backup, notifications, etc.)
  - `templates/`: Jinja2 templates
  - `static/`: CSS, JS, and assets
- `config.py`: App configuration and versioning
- `migrations/`: Alembic database migrations
- `tests/`: Pytest test suite

---

## Common Workflows

### Database Management
- **Initialize:** `flask db init`
- **Migrate:** `flask db migrate -m "Description"`
- **Upgrade:** `flask db upgrade`

### Local Development
1. **Environment:** `python -m venv venv && source venv/bin/activate`
2. **Install:** `pip install -r requirements.txt`
3. **Run:** `python run.py`
4. **Default Credentials:** `admin` / `admin`

### Release Process
1. Update `APP_VERSION` in `config.py`.
2. Commit version bump to `dev`.
3. Merge `dev` to `main`.
4. Tag release: `git tag v0.X.0 && git push origin v0.X.0`.
5. GitHub Actions handles multi-platform Docker builds automatically.
