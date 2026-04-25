from datetime import datetime

THRESHOLDS = {
    "temperature": {"min": 15, "max": 35},
    "humidity": {"min": 40, "max": 80},
    "light_level": {"min": 300, "max": 800},
}

def check_reading(reading) -> dict:
    alerts = []
    status = "healthy"

    if reading.temperature is not None:
        if reading.temperature < THRESHOLDS["temperature"]["min"]:
            alerts.append("🥶 Temperature too low!")
            status = "warning"
        elif reading.temperature > THRESHOLDS["temperature"]["max"]:
            alerts.append("🔥 Temperature too high!")
            status = "warning"

    if reading.humidity is not None:
        if reading.humidity < THRESHOLDS["humidity"]["min"]:
            alerts.append("🏜️ Humidity too low — air is too dry!")
            status = "warning"
        elif reading.humidity > THRESHOLDS["humidity"]["max"]:
            alerts.append("💦 Humidity too high — risk of mold!")
            status = "warning"

    if reading.light_level is not None:
        if reading.light_level < THRESHOLDS["light_level"]["min"]:
            alerts.append("🌑 Not enough light!")
            status = "warning"
        elif reading.light_level > THRESHOLDS["light_level"]["max"]:
            alerts.append("☀️ Too much direct light!")
            status = "warning"

    if not alerts:
        alerts.append("✅ Everything looks great!")

    return {"status": status, "alerts": alerts}


def check_watering(watering_logs) -> dict:
    if not watering_logs:
        return {"status": "warning", "alerts": ["💧 Plant has never been watered!"]}

    last_watered = max(log.watered_at for log in watering_logs)
    days_since = (datetime.utcnow() - last_watered).days

    if days_since >= 3:
        return {
            "status": "warning",
            "alerts": [f"💧 Plant hasn't been watered in {days_since} days!"]
        }

    return {
        "status": "healthy",
        "alerts": [f"✅ Last watered {days_since} day(s) ago"]
    }
