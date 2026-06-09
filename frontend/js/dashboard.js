window.onload = loadStats;

async function loadStats(){

    const response =
    await fetch(
        `${API_BASE_URL}/dashboard/stats`
    );

    const data =
    await response.json();

    document.getElementById(
        "products"
    ).innerText =
    data.total_products;

    document.getElementById(
        "categories"
    ).innerText =
    data.total_categories;

    document.getElementById(
        "stock"
    ).innerText =
    data.total_stock;
}