/**
 * Generates a string representing someone screaming while falling from a building
 * @param {number} floor - The floor number from which the person is falling
 * @returns {string} A string of screams, where:
 *                   - "Aa~ " repeats for each floor passed during the fall
 *                   - "Pa!" represents hitting the ground
 *                   - "Aa!" is added at the end if falling from 6th floor or below
 * @example
 * sc(3)  // returns "Aa~ Aa~ Pa! Aa!"
 * sc(7)  // returns "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!"
 * sc(1)  // returns ""
 */
function sc(floor) {
    // Return empty string for ground floor or below
    if (floor <= 1) return "";
    
    // Build the scream string:
    // 1. Repeat "Aa~ " for each floor passed (floor - 1 times)
    // 2. Add "Pa!" for the impact
    // 3. Add "Aa!" only if falling from 6th floor or below
    return "Aa~ ".repeat(floor - 1) + "Pa!" + (floor <= 6 ? " Aa!" : "");
}

// Driver code to test the function
console.log(sc(2));  // "Aa~ Pa! Aa!"
console.log(sc(6));  // "Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!"
console.log(sc(7));  // "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!"
console.log(sc(1));  // ""
console.log(sc(0));  // ""
