from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import PlanRequest
from app.services import llm_service, zwo_service, intervals_service

router = APIRouter()

@router.post("/generate-and-upload")
async def generate_and_upload_plan(request: PlanRequest):
    try:
        # 1. 从 intervals.icu 获取运动员当前的FTP
        athlete_info = intervals_service.get_athlete_data(request.athlete_id, request.api_key)
        # 如果找不到FTP，则默认为250
        ftp = athlete_info.get("ftp", 250) 

        # 2. 使用LLM生成训练计划
        training_plan = llm_service.generate_training_plan_from_llm(
            goal=request.goal,
            weeks=request.weeks,
            days_per_week=request.days_per_week,
            hours_per_week=request.hours_per_week,
            ftp=ftp
        )

        # 3. 将每日训练转换为ZWO文件并准备上传
        workouts_for_upload =
        for daily_workout in training_plan.workouts:
            zwo_content = zwo_service.generate_zwo_file_content(daily_workout)
            workouts_for_upload.append({
                "category": "WORKOUT",
                "start_date_local": f"{daily_workout.day}T00:00:00",
                "name": daily_workout.title,
                "description": daily_workout.coach_notes,
                "type": "Ride",
                "filename": f"{daily_workout.title.replace(' ', '_')}.zwo",
                "file_contents": zwo_content
            })

        # 4. 将训练上传到 intervals.icu
        upload_result = intervals_service.upload_workouts_to_intervals(
            athlete_id=request.athlete_id,
            api_key=request.api_key,
            workouts=workouts_for_upload
        )
        
        return {
            "message": "训练计划已成功生成并上传！",
            "plan_details": training_plan,
            "upload_status": upload_result
        }

    except Exception as e:
        # 记录异常会更有帮助
        print(f"发生错误: {e}")
        raise HTTPException(status_code=500, detail=str(e))