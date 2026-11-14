import os
from datetime import timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = PROJECT_ROOT / "templates" / "schedule_of_loss_template.xlsx"
DATA_DIR = PROJECT_ROOT / "data"

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

BATCH_MAX_AGE = timedelta(hours=24)
MAX_FILES_PER_BATCH = 20
MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB
MAX_IMAGE_SIDE = 3000

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png"}
CORS_ORIGINS = ["http://localhost:5173"]