async function getProducts() {
    return fetch("/json").then((res) => res.json())
}

function formatToIDR(price) {
    return new Intl.NumberFormat('id-ID', {
        style: 'currency',
        currency: 'IDR',
        minimumFractionDigits: 0
    }).format(price);
}

async function refreshProducts() {
    document.getElementById("product_cards").innerHTML = "";
    document.getElementById("product_cards").className = "";
    const products = await getProducts();
    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        classNameString = "mt-4 flex justify-center items-center";
        htmlString = `
        <img src="/static/empty-box.png" alt="empty box" class="max-w-36 md:max-w-64">
        <div class="max-w-64">
            <h1 class="text-lg md:text-xl font-semibold">No Products Found</h1>
            <h2 class="text-neutral-500 mt-2">
                It looks like you haven't registered any products yet. Start adding some to see them here!
            </h2>
        </div>
        `;
    } else {
        classNameString = "grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3 md:gap-5 mt-4"
        products.forEach((item) => {
            htmlString += `
            <div class="mx-auto rounded-xl shadow hover:shadow-lg max-w-52 transition duration-300">
                <a href="/json/${item.pk}">
                    <img src="/media/${item.fields.image}" class="w-full rounded-t-xl">
                    <div class="px-3 py-2 flex flex-col gap-2">
                        <h1 class="font-semibold">${item.fields.name}</h1>
                        <h2 class="font-bold text-sm md:text-lg">${formatToIDR(item.fields.price)}</h2>
                    </div>
                </a>
                <div class="px-3 py-2 flex flex-col gap-2">
                    <a href="/edit/${item.pk}"
                        class="w-full py-2 bg-blue-500 rounded-xl font-semibold text-white text-center hover:shadow hover:bg-blue-600 transition duration-300">
                        <i class="fa-solid fa-pencil mr-2"></i>
                        Edit
                    </a>
                    <a href="/delete/${item.pk}"
                        class="w-full py-2 bg-red-500 rounded-xl font-semibold text-white text-center hover:shadow hover:bg-red-600 transition duration-300">
                        <i class="fa-solid fa-trash mr-2"></i>
                        Delete
                    </a>
                </div>
            </div>
            `;
        });
    }
    document.getElementById("product_cards").className = classNameString;
    document.getElementById("product_cards").innerHTML = htmlString;
}
refreshProducts();

const modal = document.getElementById('modal');
const modalContent = document.getElementById('modalContent');

function showModal() {
    const modal = document.getElementById('modal');
    const modalContent = document.getElementById('modalContent');

    modal.classList.remove('hidden');
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('modal');
    const modalContent = document.getElementById('modalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalButton").addEventListener("click", hideModal);

function addProduct() {
    fetch("/create-ajax", {
        method: "POST",
        body: new FormData(document.querySelector('#productForm')),
    }).then(response => refreshProducts())

    document.getElementById("productForm").reset();
    hideModal();

    return false;
}

document.getElementById("submitProductForm").onclick = addProduct