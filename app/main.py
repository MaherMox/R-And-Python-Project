from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from app.database import Base, engine
from app.models.user import User
from app.models.project import Project
from app.models.task import Task
from app.routes.users import router as users_router
from app.routes.projects import router as projects_router
from app.routes.tasks import router as tasks_router
from app.core.logger import logger
from app.core.monitoring import log_request, get_monitoring, reset_monitoring


app = FastAPI(title="Task Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(projects_router)
app.include_router(tasks_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_request(
        endpoint=request.url.path,
        status_code=response.status_code,
        duration=round(process_time, 4)
    )

    logger.info(
        f"{request.method} {request.url} - Status: {response.status_code} - Time: {process_time:.4f}s"
    )

    return response


@app.get("/")
def root():
    return {"message": "Project is working 🚀"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Task Management System is running"
    }


@app.get("/monitoring")
def monitoring_dashboard():
    return get_monitoring()


@app.delete("/monitoring/reset")
def reset_monitoring_dashboard():
    reset_monitoring()
    return {"message": "Monitoring dashboard reset successfully"}