from pydantic import BaseModel, Field
from typing import Literal, Optional, List

class WorkoutBlock(BaseModel):
    type: Literal = Field(..., description="训练块的类型")
    duration_seconds: int = Field(..., gt=0, description="训练块的持续时间（秒）")
    power_start_percent_ftp: float = Field(..., ge=0, le=3, description="起始功率，以FTP百分比表示 (例如, 0.95 代表 95%)")
    power_end_percent_ftp: Optional[float] = Field(None, ge=0, le=3, description="结束功率，用于Ramp, Warmup, Cooldown")
    repeat: Optional[int] = Field(None, gt=0, description="IntervalsT的重复次数")
    off_duration_seconds: Optional[int] = Field(None, gt=0, description="IntervalsT的休息持续时间（秒）")
    off_power_percent_ftp: Optional[float] = Field(None, ge=0, le=3, description="IntervalsT的休息功率")
    cadence: Optional[int] = Field(None, description="目标踏频 (RPM)")

class DailyWorkout(BaseModel):
    day: str = Field(..., description="训练日期，格式为 YYYY-MM-DD")
    title: str = Field(..., description="训练标题，例如 'VO2 Max 间歇'")
    coach_notes: str = Field("", description="AI生成的教练笔记，解释训练目的")
    blocks: List

class TrainingPlan(BaseModel):
    plan_name: str
    workouts: List

class PlanRequest(BaseModel):
    athlete_id: str
    api_key: str
    goal: str
    weeks: int
    days_per_week: int
    hours_per_week: int