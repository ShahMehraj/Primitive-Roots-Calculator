document.addEventListener("DOMContentLoaded", function () {
    const inputNumber = document.getElementById("inputNumber");
    const findRootsBtn = document.getElementById("findRootsBtn");
    const result = document.getElementById("result");

    findRootsBtn.addEventListener("click", function () {
        const N = parseInt(inputNumber.value);

        // Check if N is a positive integer
        if (isNaN(N) || N <= 0) {
            result.innerHTML = "Please enter a valid positive number.";
            return;
        }

        // Send the N value to the server for calculation
        fetch("/find_primitive_roots", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ N: N })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                result.innerHTML = "Primitive Roots: " + data.primitive_roots.join(", ");
            } else {
                result.innerHTML = "No primitive roots found for " + N;
            }
        })
        .catch(error => {
            console.error(error);
            result.innerHTML = "An error occurred while processing the request.";
        });
    });
});
