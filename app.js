const $ = (id) => document.getElementById(id);

function showMessage(text, type = "info") {
    const box = $("message");
    if (!box) return;
    box.textContent = text;
    box.className = "message " + type;
}

const saveButton = $("saveWeightBtn");
const weightInput = $("manualWeight");

if (saveButton) {
    saveButton.addEventListener("click", async () => {
        const value = Number(weightInput ? weightInput.value : NaN);

        if (!Number.isFinite(value) || value < 20 || value > 300) {
            showMessage("Enter a valid weight between 20 and 300 kg.", "error");
            return;
        }

        saveButton.disabled = true;
        saveButton.textContent = "Saving...";

        try {
            const response = await fetch("/api/weight/save", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    weight: value,
                    source: "Manual"
                })
            });

            let data;
            try {
                data = await response.json();
            } catch (_) {
                throw new Error("Server returned an invalid response. Check the Flask terminal for the error.");
            }

            if (!response.ok || !data.success) {
                throw new Error(data.message || "Unable to save weight.");
            }

            const record = data.record;
            $("bmi").textContent = Number(record.bmi).toFixed(1);
            $("bmiStatus").textContent = record.bmi_status;
            $("goal").textContent = record.health_goal;
            $("calories").textContent = record.calories + " kcal";

            showMessage(
                "Weight saved successfully. Your new food recommendations were generated.",
                "success"
            );

            setTimeout(() => {
                window.location.href = "/dashboard";
            }, 1000);
        } catch (error) {
            showMessage(error.message || "Unable to save weight.", "error");
        } finally {
            saveButton.disabled = false;
            saveButton.textContent = "▣ Save Weight & Generate Recommendations";
        }
    });
}
