def get_ai_diagnosis(plant_name: str, health_data: dict) -> str:
    sensor = health_data["sensor_health"]
    watering = health_data["watering_health"]
    alerts = sensor["alerts"] + watering["alerts"]
    
    issues = []
    fixes = []

    for alert in alerts:
        if "Temperature too high" in alert:
            issues.append("overheating")
            fixes.append("move it to a cooler spot or add shade")
        elif "Temperature too low" in alert:
            issues.append("cold stress")
            fixes.append("move it to a warmer location away from drafts")
        elif "Humidity too low" in alert:
            issues.append("dry air stress")
            fixes.append("mist the leaves daily or place a water tray nearby")
        elif "Humidity too high" in alert:
            issues.append("mold risk")
            fixes.append("improve air circulation and reduce watering")
        elif "Not enough light" in alert:
            issues.append("light deficiency")
            fixes.append("move it closer to a window or add a grow light")
        elif "Too much direct light" in alert:
            issues.append("light overexposure")
            fixes.append("move it away from direct sunlight or use a curtain")
        elif "never been watered" in alert:
            issues.append("dehydration")
            fixes.append("water it immediately with about 200ml and check soil moisture daily")
        elif "hasn't been watered" in alert:
            issues.append("underwatering")
            fixes.append("give it a good watering today and set a reminder every 2 days")
        elif "Everything looks great" in alert:
            return f"✅ {plant_name} is in perfect condition! All sensor readings are within healthy ranges. Keep up the good care — maintain the current watering schedule and environment."

    if not issues:
        return f"✅ {plant_name} looks healthy! Keep monitoring regularly."

    issue_text = " and ".join(issues)
    fix_text = ", and ".join(fixes)

    return (
        f"⚠️ {plant_name} is experiencing {issue_text}. "
        f"To fix this: {fix_text}. "
        f"Monitor the readings over the next 24 hours to confirm improvement."
    )