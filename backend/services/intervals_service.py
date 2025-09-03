import requests
from typing import List, Dict, Any

BASE_URL = "https://intervals.icu/api/v1"

def get_athlete_data(athlete_id: str, api_key: str) -> Dict[str, Any]:
    """获取运动员的基本数据，如FTP。"""
    url = f"{BASE_URL}/athlete/{athlete_id}"
    # intervals.icu API 使用 HTTP Basic Auth, 用户名为 "API_KEY"
    response = requests.get(url, auth=("API_KEY", api_key))
    response.raise_for_status()
    return response.json()

def upload_workouts_to_intervals(athlete_id: str, api_key: str, workouts: List[Dict[str, Any]]):  # 修复：添加了类型注解
    """将训练计划列表上传到 intervals.icu 日历。"""
    url = f"{BASE_URL}/athlete/{athlete_id}/events"
    headers = {"Content-Type": "application/json"}
    
    uploaded_count = 0
    for workout in workouts:
        try:
            response = requests.post(url, auth=("API_KEY", api_key), json=workout, headers=headers)
            response.raise_for_status()
            uploaded_count += 1
        except requests.exceptions.RequestException as e:
            print(f"上传训练失败: {workout.get('name', 'Unknown')}, 错误: {e}")
            # 继续上传其他训练而不是完全失败
            continue
    
    return {"status": "success", "uploaded_count": uploaded_count, "total_workouts": len(workouts)}