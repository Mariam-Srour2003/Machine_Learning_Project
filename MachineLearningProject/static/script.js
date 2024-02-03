function search() {
    const userInput = document.getElementById('userInput').value;

    $.post('http://127.0.0.1:5000/predict', { user_input: userInput }, function (data) {
        const predictionsDiv = document.getElementById('predictions');
        predictionsDiv.innerHTML = "<h2>Top 5 Predictions:</h2>";

        // Create a table
        const table = document.createElement('table');
        table.className = 'predictions-table';

        // Create table header
        const headerRow = table.createTHead().insertRow(0);
        const headerLabels = ['Label', 'Probability', 'Description'];
        headerLabels.forEach(label => {
            const th = document.createElement('th');
            th.textContent = label;
            headerRow.appendChild(th);
        });

        // Create table body
        const tbody = table.createTBody();
        for (const prediction of data) {
            const label = prediction.label;
            const probability = prediction.probability.toFixed(5);
            const description = prediction.description;

            // Create a new row for each prediction
            const row = tbody.insertRow();
            const cellLabel = row.insertCell(0);
            const cellProbability = row.insertCell(1);
            const cellDescription = row.insertCell(2);

            // Fill the cells with data
            cellLabel.textContent = label;
            cellProbability.textContent = probability;
            cellDescription.textContent = description;
        }

        // Append the table to the predictionsDiv
        predictionsDiv.appendChild(table);
    });
}

