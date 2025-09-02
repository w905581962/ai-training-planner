import xml.etree.ElementTree as ET
from typing import List
from app.models.pydantic_models import DailyWorkout, WorkoutBlock

def generate_zwo_file_content(workout: DailyWorkout) -> str:
    """从DailyWorkout对象生成.zwo文件的XML内容。"""
    root = ET.Element("workout_file")
    
    ET.SubElement(root, "author").text = "AI Training Planner"
    ET.SubElement(root, "name").text = workout.title
    ET.SubElement(root, "description").text = workout.coach_notes
    ET.SubElement(root, "sportType").text = "bike"
    
    workout_element = ET.SubElement(root, "workout")
    
    for block in workout.blocks:
        attributes = {}
        # ZWO格式要求首字母大写
        block_type_zwo = block.type
        
        if block_type_zwo in:
            attributes = {
                "Duration": str(block.duration_seconds),
                "PowerLow": str(block.power_start_percent_ftp),
                "PowerHigh": str(block.power_end_percent_ftp)
            }
        elif block_type_zwo == "SteadyState":
            attributes = {
                "Duration": str(block.duration_seconds),
                "Power": str(block.power_start_percent_ftp)
            }
        elif block_type_zwo == "IntervalsT":
            attributes = {
                "Repeat": str(block.repeat),
                "OnDuration": str(block.duration_seconds),
                "OffDuration": str(block.off_duration_seconds),
                "OnPower": str(block.power_start_percent_ftp),
                "OffPower": str(block.off_power_percent_ftp)
            }
        elif block_type_zwo == "FreeRide":
             attributes = {
                "Duration": str(block.duration_seconds)
            }

        if block.cadence:
            attributes["Cadence"] = str(block.cadence)
            
        ET.SubElement(workout_element, block_type_zwo, attributes)
        
    # 美化XML输出以便阅读
    ET.indent(root, space="\t", level=0)
    return ET.tostring(root, encoding='unicode')