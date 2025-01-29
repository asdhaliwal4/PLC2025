function listFunc(a, b) {
    let arr = [];
    for (let i = a; i <= b; i++) {
        arr.push(i);
    }
    return arr;
}

// applicatorFunc computes the sum or average based on the user's choice
function applicatorFunc(inpFunc, a, b, s) {
    const nums = inpFunc(a, b);
    if (s === 's') {
        return nums.reduce((acc, num) => acc + num, 0);  
    } else {
        const sum = nums.reduce((acc, num) => acc + num, 0);
        return sum / nums.length;  
    }
}

function main() {
    const a = parseInt(prompt("Enter start of range: "), 10);
    const b = parseInt(prompt("Enter end of range: "), 10);
    const s = prompt("Enter 's' for sum or anything else for average: ").trim();

    const result = applicatorFunc(listFunc, a, b, s);
    alert("Result: " + result);
}

// Run the main function
main();
