# game-analytics-backend

Minimal FastAPI backend for processing game videos and producing analytics.

Project layout

```
game-analytics-backend/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services/
│   │     ├── video_processor.py
│   │     ├── analytics.py
│   │     ├── detector.py
│   │     └── llm_service.py
│   └── routes/
│         └── video_routes.py
│
├── uploads/
├── requirements.txt
└── .env
```

Requirements

- Windows PowerShell (instructions below use PowerShell)
- Python 3.8+

Quick start (PowerShell)

1. Open PowerShell and change to the project directory:

```powershell
cd d:\shrishail-exp\game-R\game-analytics-backend
```

2. Create and activate a virtual environment, then install dependencies:

```powershell
# allow activation for this session if needed
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; 
python -m venv .venv; 
.\.venv\Scripts\Activate.ps1; 
pip install -r .\requirements.txt
```

3. Initialize the SQLite database (creates tables):

```powershell
python -c "from app.database import Base, engine; import app.models; Base.metadata.create_all(bind=engine)"
```

4. Run the dev server:

```powershell
python -m uvicorn app.main:app --reload --port 8000
```

API

- GET / -> health/status
- POST /videos/upload -> upload a video file (form field name `file`)

Example upload (curl) — replace the path to your video:

```powershell
curl -X POST "http://127.0.0.1:8000/videos/upload" -F "file=@C:\path\to\video.mp4"
```

Notes & next steps

- Add real processing logic in `app/services/video_processor.py` and detection/analytics implementations.
- Consider adding Alembic for migrations if the schema will evolve.
- Add tests (pytest) and CI config if desired.

If you want, I can start the server in a terminal here, add a simple README badge, or add a `README.md` section demonstrating a minimal test for the upload route. Which would you like next?
