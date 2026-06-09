window.onload = loadCategories;

async function createCategory(){

    const name =
        document.getElementById(
            "categoryName"
        ).value;

    await fetch(
        `${API_BASE_URL}/categories/`,
        {
            method:"POST",

            headers:authHeaders(),

            body:JSON.stringify({
                name:name
            })
        }
    );

    loadCategories();
}

async function loadCategories(){

    const response =
    await fetch(
        `${API_BASE_URL}/categories/`
    );

    const categories =
    await response.json();

    const table =
    document.getElementById(
        "categoryTable"
    );

    table.innerHTML = "";

    categories.forEach(category=>{

        table.innerHTML += `
            <tr>
                <td>${category.id}</td>
                <td>${category.name}</td>
            </tr>
        `;
    });
}