function calculateWaterNeed(soilHumidity, plantType) {
    let message = "";
    let quantity = 0;

    if (soilHumidity < 30) {
        quantity = 5.5; // Exemple : 5.5 Litres par m²
        message = `Attention : Sol très sec. Arrosage recommandé : ${quantity}L/m²`;
    } else if (soilHumidity < 60) {
        quantity = 2.0;
        message = `Sol modérément humide. Apport conseillé : ${quantity}L/m²`;
    } else {
        message = "Humidité optimale. Pas d'arrosage nécessaire.";
    }

    document.getElementById('irrStatus').textContent = message;
}