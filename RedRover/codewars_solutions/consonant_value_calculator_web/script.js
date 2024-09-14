function charValue(char) {
    return char.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
}

function substringValue(substring) {
    let totalValue = 0;
    for (let char of substring) {
        totalValue += charValue(char);
    }
    return totalValue;
}

function solve(userString) {
    const vowels = new Set("aeiou");
    const consonantSubstrings = [];
    let currentSubstring = "";

    for (let character of userString) {
        if (!vowels.has(character)) {
            currentSubstring += character;
        } else {
            if (currentSubstring) {
                consonantSubstrings.push(currentSubstring);
                currentSubstring = "";
            }
        }
    }

    if (currentSubstring) {
        consonantSubstrings.push(currentSubstring);
    }

    if (consonantSubstrings.length === 0) {
        return { maxValue: 0, details: [] };
    }

    let maxValue = 0;
    const details = [];

    for (let sub of consonantSubstrings) {
        const subValue = substringValue(sub);
        details.push({ substring: sub, value: subValue });
        if (subValue > maxValue) {
            maxValue = subValue;
        }
    }

    return { maxValue, details };
}

function displayResults() {
    const userInput = document.getElementById("userInput").value.toLowerCase();
    const result = solve(userInput);

    // Display the result
    document.getElementById("result").innerText = `Highest Consonant Substring Value: ${result.maxValue}`;

    // Display the details
    let visualization = "<h3>Details of Consonant Substrings:</h3><ul>";
    for (const detail of result.details) {
        visualization += `<li>Substring: "${detail.substring}", Value: ${detail.value}</li>`;
    }
    visualization += "</ul>";
    document.getElementById("visualization").innerHTML = visualization;
}

// Event listener for the button click
document.getElementById("calculateButton").addEventListener("click", displayResults);

// Event listener for the Enter key press
document.getElementById("userInput").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        displayResults();
    }
});
