async function stockIn(){

    const product_id =
    parseInt(
        document.getElementById(
            "productId"
        ).value
    );

    const quantity =
    parseInt(
        document.getElementById(
            "quantity"
        ).value
    );

    await fetch(
        `${API_BASE_URL}/inventory/stock-in`,
        {
            method:"POST",

            headers:authHeaders(),

            body:JSON.stringify({
                product_id,
                quantity
            })
        }
    );

    alert(
        "Stock Added"
    );
}