from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import plan

app = FastAPI(title="AI训练计划生成器")

# CORS 中间件
app.add_middleware(
    CORSMiddleware,
    # 在生产环境中，应将此限制为您的前端域名
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plan.router, prefix="/api/v1", tags=["plan"])

@app.get("/")
def read_root():
    return {"message": "欢迎使用AI训练计划生成器API"}