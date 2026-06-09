window.onload = loadReport;

async function loadReport(){

    const response =
    await fetch(
        `${API_BASE_URL}/reports/inventory-value`
    );

    const data =
    await response.json();

    document.getElementById(
        "reportData"
    ).innerText =
    JSON.stringify(
        data,
        null,
        2
    );
}