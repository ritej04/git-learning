function saveSettings() {
    const settings = {
        autoIrrigation:
 document.getElementById('autoIrrigateToggle').checked,
        threshold: document.getElementById('humThreshold').value
    };

    fetch('/api/save-settings', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(settings)
    }).then(() => {
        document.getElementById('toast').classList.add('visible'); // Show success toast
    });
}