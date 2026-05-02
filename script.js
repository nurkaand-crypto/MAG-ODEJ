// Каталог товаров
const products = [
    // Одежда
    { id: 1, name: 'Базовая футболка', category: 'clothes', sizes: ['S', 'M', 'L', 'XL'], price: 599, image: 'images/tshirt.jpg' },
    { id: 2, name: 'Джинсы классические', category: 'clothes', sizes: ['S', 'M', 'L', 'XL', 'XXL'], price: 2499, image: 'images/jeans.jpg' },
    { id: 3, name: 'Рубашка хлопковая', category: 'clothes', sizes: ['S', 'M', 'L', 'XL', 'XXL'], price: 1899, image: 'images/shirt.jpg' },
    { id: 4, name: 'Толстовка спортивная', category: 'clothes', sizes: ['XS', 'S', 'M', 'L', 'XL'], price: 1799, image: 'images/hoodie.jpg' },
    { id: 5, name: 'Платье летнее', category: 'clothes', sizes: ['XS', 'S', 'M', 'L'], price: 2199, image: 'images/dress.jpg' },
    { id: 6, name: 'Юбка миди', category: 'clothes', sizes: ['S', 'M', 'L'], price: 1599, image: 'images/skirt.jpg' },
    // Обувь
    { id: 7, name: 'Кроссовки спортивные', category: 'shoes', sizes: ['36', '37', '38', '39', '40', '41', '42', '43'], price: 3499, image: 'images/sneakers.jpg' },
    { id: 8, name: 'Кеды классические', category: 'shoes', sizes: ['36', '37', '38', '39', '40', '41', '42'], price: 1999, image: 'images/sneakers_classic.jpg' },
    { id: 9, name: 'Сапоги зимние', category: 'shoes', sizes: ['36', '37', '38', '39', '40', '41'], price: 4999, image: 'images/boots.jpg' },
    { id: 10, name: 'Туфли офисные', category: 'shoes', sizes: ['36', '37', '38', '39', '40', '41', '42'], price: 2799, image: 'images/heels.jpg' },
    { id: 11, name: 'Сандалии летние', category: 'shoes', sizes: ['36', '37', '38', '39', '40', '41', '42'], price: 899, image: 'images/sandals.jpg' },
    // Аксессуары
    { id: 12, name: 'Шапка вязаная', category: 'accessories', sizes: ['all-sizes'], price: 699, image: 'images/hat.jpg' },
    { id: 13, name: 'Шарф теплый', category: 'accessories', sizes: ['all-sizes'], price: 1099, image: 'images/scarf.jpg' },
    { id: 14, name: 'Перчатки кожаные', category: 'accessories', sizes: ['M', 'L'], price: 1499, image: 'images/gloves.jpg' },
    { id: 15, name: 'Сумка кожаная', category: 'accessories', sizes: ['all-sizes'], price: 3999, image: 'images/bag.jpg' },
    { id: 16, name: 'Ремень кожаный', category: 'accessories', sizes: ['all-sizes'], price: 899, image: 'images/belt.jpg' },
];

// Корзина
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Обновляем счётчик корзины
function updateCartCount() {
    const count = cart.length;
    document.querySelectorAll('.cart-count').forEach(el => {
        el.textContent = count;
    });
}

// Инициализация при загрузке
document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();
    
    // Если это страница товаров
    if (document.getElementById('productsGrid')) {
        renderProducts(products);
        setupFilters();
    }
    
    // Если это страница корзины
    if (document.getElementById('basketItems')) {
        renderBasket();
    }
});

// Рендеринг товаров
function renderProducts(productsToRender) {
    const grid = document.getElementById('productsGrid');
    grid.innerHTML = '';
    
    productsToRender.forEach(product => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}" style="width: 100%; height: 200px; object-fit: cover;">
            </div>
            <div class="product-info">
                <div class="product-category">${getCategoryLabel(product.category)}</div>
                <div class="product-name">${product.name}</div>
                <div class="product-size">Размеры: ${getSizesDisplay(product.sizes)}</div>
                <div class="product-footer">
                    <div class="product-price">${product.price} ₽</div>
                    <button class="product-button" onclick="openProductModal(${product.id})">Выбрать</button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

// Получить названия размеров
function getSizesDisplay(sizes) {
    if (sizes.includes('all-sizes')) return 'Один размер';
    return sizes.join(', ').slice(0, 15) + '...';
}

// Получить название категории
function getCategoryLabel(category) {
    const labels = {
        'clothes': 'Одежда',
        'shoes': 'Обувь',
        'accessories': 'Аксессуары'
    };
    return labels[category] || category;
}

// Открыть модальное окно товара
function openProductModal(productId) {
    const product = products.find(p => p.id === productId);
    if (!product) return;
    
    const modal = document.getElementById('productModal');
    const sizeSelect = document.getElementById('sizeSelect');
    const quantityInput = document.getElementById('quantityInput');
    
    // Заполняем информацию
    document.getElementById('modalImage').src = product.image;
    document.getElementById('modalImage').alt = product.name;
    document.getElementById('modalTitle').textContent = product.name;
    document.getElementById('modalDescription').textContent = `Категория: ${getCategoryLabel(product.category)}`;
    document.getElementById('modalPrice').textContent = product.price;
    
    // Заполняем размеры
    sizeSelect.innerHTML = '<option value="">Выберите размер</option>';
    if (!product.sizes.includes('all-sizes')) {
        product.sizes.forEach(size => {
            const option = document.createElement('option');
            option.value = size;
            option.textContent = size;
            sizeSelect.appendChild(option);
        });
    } else {
        const option = document.createElement('option');
        option.value = 'one-size';
        option.textContent = 'Один размер';
        sizeSelect.appendChild(option);
    }
    
    quantityInput.value = 1;
    
    // Обработчик кнопки
    document.getElementById('addToCartBtn').onclick = () => {
        const size = sizeSelect.value;
        if (!size) {
            alert('Пожалуйста, выберите размер');
            return;
        }
        
        const quantity = parseInt(quantityInput.value);
        addToCart(productId, size, quantity);
        modal.style.display = 'none';
    };
    
    modal.style.display = 'block';
}

// Закрыть модальное окно
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('productModal');
    if (modal) {
        const closeBtn = modal.querySelector('.close');
        closeBtn.onclick = () => {
            modal.style.display = 'none';
        };
        
        window.onclick = (event) => {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        };
    }
});

// Добавить в корзину
function addToCart(productId, size, quantity) {
    const product = products.find(p => p.id === productId);
    if (!product) return;
    
    const cartItem = {
        id: Date.now(),
        productId,
        name: product.name,
        size,
        price: product.price,
        quantity,
        image: product.image
    };
    
    cart.push(cartItem);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert(`✓ ${product.name} добавлен в корзину!`);
}

// Фильтры товаров
function setupFilters() {
    const categoryFilters = document.querySelectorAll('.category-filter');
    const sizeFilters = document.querySelectorAll('.size-filter');
    const priceMin = document.getElementById('priceMin');
    const priceMax = document.getElementById('priceMax');
    const minPriceDisplay = document.getElementById('minPrice');
    const maxPriceDisplay = document.getElementById('maxPrice');
    const filterReset = document.querySelector('.filter-reset');
    
    // Обновить отображение цены
    const updatePriceDisplay = () => {
        minPriceDisplay.textContent = priceMin.value;
        maxPriceDisplay.textContent = priceMax.value;
        applyFilters();
    };
    
    priceMin.addEventListener('input', updatePriceDisplay);
    priceMax.addEventListener('input', updatePriceDisplay);
    
    categoryFilters.forEach(filter => {
        filter.addEventListener('change', () => {
            // Если выбран "Все товары", отключить остальные
            if (filter.value === 'all' && filter.checked) {
                categoryFilters.forEach(f => {
                    if (f.value !== 'all') f.checked = false;
                });
            } else if (filter.value !== 'all' && filter.checked) {
                document.querySelector('[value="all"].category-filter').checked = false;
            }
            applyFilters();
        });
    });
    
    sizeFilters.forEach(filter => {
        filter.addEventListener('change', () => {
            // Если выбран "Все размеры", отключить остальные
            if (filter.value === 'all-sizes' && filter.checked) {
                sizeFilters.forEach(f => {
                    if (f.value !== 'all-sizes') f.checked = false;
                });
            } else if (filter.value !== 'all-sizes' && filter.checked) {
                document.querySelector('[value="all-sizes"].size-filter').checked = false;
            }
            applyFilters();
        });
    });
    
    filterReset.addEventListener('click', () => {
        categoryFilters.forEach(f => f.checked = f.value === 'all');
        sizeFilters.forEach(f => f.checked = f.value === 'all-sizes');
        priceMin.value = 0;
        priceMax.value = 10000;
        updatePriceDisplay();
    });
}

// Применить фильтры
function applyFilters() {
    const selectedCategories = [];
    const selectedSizes = [];
    const minPrice = parseInt(document.getElementById('priceMin').value);
    const maxPrice = parseInt(document.getElementById('priceMax').value);
    
    document.querySelectorAll('.category-filter:checked').forEach(filter => {
        if (filter.value !== 'all') {
            selectedCategories.push(filter.value);
        }
    });
    
    document.querySelectorAll('.size-filter:checked').forEach(filter => {
        if (filter.value !== 'all-sizes') {
            selectedSizes.push(filter.value);
        }
    });
    
    // Если ничего не выбрано в категориях, показываем все
    let filtered = products;
    
    if (selectedCategories.length > 0) {
        filtered = filtered.filter(p => selectedCategories.includes(p.category));
    }
    
    // Фильтр по цене
    filtered = filtered.filter(p => p.price >= minPrice && p.price <= maxPrice);
    
    // Фильтр по размерам
    if (selectedSizes.length > 0) {
        filtered = filtered.filter(p => {
            return selectedSizes.some(size => p.sizes.includes(size));
        });
    }
    
    renderProducts(filtered);
}

// Рендеринг корзины
function renderBasket() {
    const basketItems = document.getElementById('basketItems');
    const emptyMessage = document.getElementById('emptyBasket');
    const totalItems = document.getElementById('totalItems');
    const subtotal = document.getElementById('subtotal');
    const total = document.getElementById('total');
    
    if (cart.length === 0) {
        basketItems.style.display = 'none';
        emptyMessage.style.display = 'block';
        totalItems.textContent = '0';
        subtotal.textContent = '0 ₽';
        total.textContent = '0 ₽';
        return;
    }
    
    basketItems.style.display = 'flex';
    emptyMessage.style.display = 'none';
    basketItems.innerHTML = '';
    
    let totalPrice = 0;
    
    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        totalPrice += itemTotal;
        
        const itemElement = document.createElement('div');
        itemElement.className = 'basket-item';
        itemElement.innerHTML = `
            <div class="item-image">
                <img src="${item.image}" alt="${item.name}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 4px;">
            </div>
            <div class="item-details">
                <div class="item-name">${item.name}</div>
                <div class="item-size">Размер: ${item.size}</div>
                <div class="item-price">${item.price} ₽</div>
            </div>
            <div class="item-controls">
                <div class="quantity-control">
                    <button onclick="decreaseQuantity(${item.id})">−</button>
                    <input type="number" value="${item.quantity}" readonly>
                    <button onclick="increaseQuantity(${item.id})">+</button>
                </div>
                <div style="margin-left: 1rem; font-weight: bold; color: #ff6b35;">
                    ${itemTotal} ₽
                </div>
                <button class="remove-btn" onclick="removeFromCart(${item.id})">Удалить</button>
            </div>
        `;
        basketItems.appendChild(itemElement);
    });
    
    const delivery = 500;
    const totalWithDelivery = totalPrice + delivery;
    
    totalItems.textContent = cart.length;
    subtotal.textContent = totalPrice + ' ₽';
    total.textContent = totalWithDelivery + ' ₽';
    
    // Сохраняем общую сумму для оформления заказа
    window.totalAmount = totalWithDelivery;
}

// Изменить количество
function increaseQuantity(itemId) {
    const item = cart.find(i => i.id === itemId);
    if (item) {
        item.quantity++;
        localStorage.setItem('cart', JSON.stringify(cart));
        renderBasket();
    }
}

function decreaseQuantity(itemId) {
    const item = cart.find(i => i.id === itemId);
    if (item && item.quantity > 1) {
        item.quantity--;
        localStorage.setItem('cart', JSON.stringify(cart));
        renderBasket();
    }
}

// Удалить из корзины
function removeFromCart(itemId) {
    cart = cart.filter(item => item.id !== itemId);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    renderBasket();
}

// Применить промокод
document.addEventListener('DOMContentLoaded', () => {
    const applyPromoBtn = document.getElementById('applyPromo');
    if (applyPromoBtn) {
        applyPromoBtn.addEventListener('click', applyPromoCode);
    }
});

function applyPromoCode() {
    const promoCode = document.getElementById('promoCode').value.trim().toUpperCase();
    
    const promoCodes = {
        'SKIDKA10': 0.1,
        'SKIDKA20': 0.2,
        'WELCOME': 0.05
    };
    
    if (promoCodes[promoCode]) {
        const discount = window.totalAmount * promoCodes[promoCode];
        const newTotal = window.totalAmount - discount;
        
        document.getElementById('total').textContent = Math.round(newTotal) + ' ₽';
        alert(`✓ Промокод принят! Скидка: ${Math.round(discount)} ₽`);
        window.totalAmount = newTotal;
    } else {
        alert('❌ Неверный промокод!');
    }
}
