// Handle form submission
document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();  // Prevent form from refreshing the page

    // Get input values
    const formData = {
        Gender: document.getElementById('gender').value,
        Age: document.getElementById('age').value,
        Height: document.getElementById('height').value,
        Weight: document.getElementById('weight').value,
        Duration: document.getElementById('duration').value,
        Heart_Rate: document.getElementById('heart_rate').value,
        Body_Temp: document.getElementById('body_temp').value
    };

    // Send data to Flask API
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(formData).toString()  // Use URLSearchParams to encode form data
        });

        const result = await response.json();

        if (result.error) {
            document.getElementById('result').innerText = `Error: ${result.error}`;
        } else {
            // Check if 'calories_burned' is present in the response
            if (result.calories_burned !== undefined) {
                document.getElementById('result').innerText = `Predicted Calories Burned: ${result.calories_burned} kcal`;
            } else {
                document.getElementById('result').innerText = "Error: Unable to retrieve prediction.";
            }
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = `Error: ${error}`;
    }
});
