window.onload = loadProducts;

async function createProduct(){

    const product = {

        sku:
        document.getElementById(
            "sku"
        ).value,

        name:
        document.getElementById(
            "name"
        ).value,

        description:
        document.getElementById(
            "description"
        ).value,

        cost_price:
        parseFloat(
            document.getElementById(
                "cost_price"
            ).value
        ),

        selling_price:
        parseFloat(
            document.getElementById(
                "selling_price"
            ).value
        ),

        minimum_stock:
        parseInt(
            document.getElementById(
                "minimum_stock"
            ).value
        ),

        category_id:
        parseInt(
            document.getElementById(
                "category_id"
            ).value
        )
    };

    await fetch(
        `${API_BASE_URL}/products/`,
        {
            method:"POST",
            headers:authHeaders(),
            body:JSON.stringify(product)
        }
    );

    loadProducts();
}

async function loadProducts(){

    const response =
    await fetch(
        `${API_BASE_URL}/products/`
    );

    const products =
    await response.json();

    const table =
    document.getElementById(
        "productTable"
    );

    table.innerHTML = "";

    products.forEach(product=>{

        table.innerHTML += `
        <tr>
            <td>${product.sku}</td>
            <td>${product.name}</td>
            <td>${product.current_stock}</td>
        </tr>
        `;
    });
}