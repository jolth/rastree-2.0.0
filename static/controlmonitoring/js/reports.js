/*
 * Copyright 2022 Jolth <jolthgs at gmail dot com>
 */
async function check_plate(plate) {
    const res = await fetch(`/controlmonitoring/check_plate?plate=${plate}`);
    return res.json();
}

async function reports(plate, started=null) {
    let endend = `${started} 23:59:59`;

    const res = await fetch(`/controlmonitoring/reports_json?plate=${plate}&started=${started}&endend=${endend}`);
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


function validateInput(element) {
    let classList = Array.from(element.classList);

    if (element.value === "") {
        applyStyle(element, false);
        return false;
    }

    if (classList.includes('error-input')) {
        applyStyle(element, false);
        return false;
    }

    return true;
}

/*
 * Functions set the current date in All the date input.
 */
function autoInputDate() {
    const now = new Date();
    now.setUTCHours(-5); // Bogotá

    Array.from(arguments)[0].forEach(e => {
        if (e.value === "") {
            e.value = now.toISOString().split('T')[0];
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const dateElements = document.querySelectorAll('input[type="date"]');
    autoInputDate(dateElements);
    
    const plateElement = document.querySelector("#plate");
    plateElement.addEventListener('change', async () => {
        const plate = plateElement.value;
        let res;

        try {
          res = await check_plate(plate);
        } catch (e) {
          console.log("Error: ", e);
        }

        applyStyle(plateElement, res.plate);
    });
    
    const buttonElement = document.querySelector('#button');
    const tableElement = document.querySelector('#table'); 
    const copyTable = tableElement.innerHTML; 

    buttonElement.addEventListener('click', async () => {
        tableElement.innerHTML = copyTable;
        let res = null;

        try {
            res = await reports(plateElement.value, dateElements[0].value);
        } catch (e) {
            console.log("Error: ", e);
        }

        if (res === undefined) {
            validateInput(plateElement, false);
        }

        if (res.length === 0) {
            tableElement.innerHTML += `<caption style="color: red">There are no reports for ${plateElement.value} of this day</caption>`
        }
        
        let tableRow = "";
        for (let row of res) {
          let tdEvent = row['name'] === "Bateria OFF" ? `<td class="danger">${row['name']}</td>` : `<td>${row['name']}</td>`;
          let position = row['position'].slice(1, -1).split(',');
          tableRow += `<tr>
                  <td>${row['placa']}</td>  
                  <td>${row['fecha']}</td>  
                  <td><a target="_blank" href="https://maps.google.com/maps?f=q&q=${position[0]},${position[1]}&z=16">${row['ubicacion']}</a></td>  
                  <td>${row['altura']}</td>  
                  <td>${row['grados']}</td>  
                  <td>${row['velocidad']}</td>  
                  ${tdEvent}
                </tr>`;
        }
        tableElement.innerHTML += `<tbody>${tableRow}</tbody>`;
    });
});
