from fastapi import FastAPI
from db.db import engine,Base
from fastapi.middleware.cors import CORSMiddleware
from routes.employee_master import router as employee_router
from routes.attendance import router as attendance_router
from routes.monitor import router as monitor_router
from routes.device import router as device_router
from routes.area import router as area_router
from routes.location_type import router as location_type_router
from routes.location_tag import router as location_tag_router
from fastapi.staticfiles import StaticFiles
Base.metadata.create_all(bind=engine)


app = FastAPI()

UPLOAD_DIRECTORY = "./uploaded_images"
app.mount("/uploaded_images", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploaded_images")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
app.include_router(employee_router)
app.include_router(attendance_router)
app.include_router(monitor_router)
app.include_router(device_router)
app.include_router(area_router)
app.include_router(location_type_router)
app.include_router(location_tag_router)
@app.get("/")
async def read_root():
    return {"status": "Ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)