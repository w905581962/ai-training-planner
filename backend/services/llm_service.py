from litellm import completion
from app.models.pydantic_models import TrainingPlan
from app.core.config import settings
import json

def generate_training_plan_from_llm(goal: str, weeks: int, days_per_week: int, hours_per_week: int, ftp: int) -> TrainingPlan:
    """使用LLM生成结构化的训练计划。"""
    
    system_prompt = f"""
    你是一位专业的自行车教练。你的任务是创建一个科学、个性化的训练计划。
    该计划必须遵循周期化（Periodization）和渐进超负荷（Progressive Overload）的原则。
    输出必须是一个严格遵循所提供的'TrainingPlan'工具模式（tool schema）的有效JSON对象。
    除了JSON对象之外，不要包含任何其他文本。
    """

    user_prompt = f"""
    请为一名运动员生成一个为期 {weeks} 周的训练计划，具体信息如下：
    - 主要目标: {goal}
    - 训练时间: 每周 {days_per_week} 天, 总计 {hours_per_week} 小时。
    - 当前FTP: {ftp} 瓦。

    请确保计划具有逻辑递进性。如果计划超过4周，请在每第4周安排一个恢复周。
    为每次训练提供标题、解释其目的的教练笔记，以及详细的训练块序列。
    功率目标必须是FTP的百分比。
    请根据今天的日期（假设是2025-09-01）开始生成训练日期。
    """

    response = completion(
        model=settings.LITELLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        tools=,
        tool_choice={"type": "function", "function": {"name": "TrainingPlan"}}
    )
    
    tool_call = response.choices.message.tool_calls
    plan_data_str = tool_call.function.arguments
    
    # LiteLLM有时会返回一个被额外引号包裹的字符串，需要解析
    plan_data = json.loads(plan_data_str)
    
    return TrainingPlan.model_validate(plan_data)