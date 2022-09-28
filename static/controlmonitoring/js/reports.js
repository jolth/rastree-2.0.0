/*
 * Copyright 2022 Jolth <jolthgs at gmail dot com>
 */
async function check_plate(plate) {
    const res = await fetch(`/controlmonitoring/check_plate?plate=${plate}`);
    return res.json();
}

function applyStyle(element, test, classStyle=null) {
    let label = document.querySelector(`label[for='${element.name}']`);

    if (test === true) {
        element.classList.remove("error-input", "success-input");
        element.classList.add("success-input");

        label.classList.remove("error");
    }

    if (test === false) {
        element.classList.remove("error-input", "success-input");
        element.classList.add("error-input");

        label.classList.add("error");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    
    const elementPlate = document.querySelector("#plate");

    elementPlate.addEventListener('change', async () => {
        const plate = elementPlate.value;
        let res;

        try {
          res = await check_plate(plate);
        } catch (e) {
          console.log("Error: ", e);
        }

        applyStyle(elementPlate, res.plate);
    });
});
