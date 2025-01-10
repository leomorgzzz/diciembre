document.addEventListener("DOMContentLoaded", function() {
    const num1 = document.getElementById("num1");
    const num2 = document.getElementById("num2");
    const result = document.getElementById("result");
    const showProcedureButton = document.getElementById("showProcedureButton");
    const hideProcedureButton = document.getElementById("hideProcedureButton");
    const procedure = document.getElementById("procedure");

    let operation = "";
    let num1Value = 0;
    let num2Value = 0;
    let resultValue = 0;

    function calculate(operator) {
        num1Value = parseFloat(num1.value);
        num2Value = parseFloat(num2.value);

        if (isNaN(num1Value) || isNaN(num2Value)) {
            result.textContent = "Resultado: Ingrese números válidos";
            return;
        }

        switch (operator) {
            case "+":
                resultValue = num1Value + num2Value;
                operation = "+";
                break;
            case "-":
                resultValue = num1Value - num2Value;
                operation = "-";
                break;
            case "*":
                resultValue = num1Value * num2Value;
                operation = "x";
                break;
            case "/":
                if (num2Value === 0) {
                    result.textContent = "Resultado: No se puede dividir por cero";
                    return;
                }
                resultValue = num1Value / num2Value;
                operation = "/";
                break;
        }

        result.textContent = `Resultado: ${resultValue}`;
        showProcedureButton.style.display = "block";
    }

    document.getElementById("sumButton").addEventListener("click", () => calculate("+"));
    document.getElementById("restButton").addEventListener("click", () => calculate("-"));
    document.getElementById("multButton").addEventListener("click", () => calculate("*"));
    document.getElementById("divButton").addEventListener("click", () => calculate("/"));

    showProcedureButton.addEventListener("click", () => {
        procedure.textContent = `${num1Value} ${operation} ${num2Value} = ${resultValue}`;
        hideProcedureButton.style.display = "block";
        showProcedureButton.style.display = "none";
    });

    hideProcedureButton.addEventListener("click", () => {
        procedure.textContent = "";
        hideProcedureButton.style.display = "none";
        showProcedureButton.style.display = "block";
    });
});