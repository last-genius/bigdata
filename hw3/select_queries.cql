// Отримувати всі відгуки за заданим product_id
SELECT review FROM products WHERE product_id = 42;

// Отримувати всі відгуки за заданим product_id та обраним star_rating
SELECT review FROM products WHERE product_id = 42 AND star_rating = 5;

// Отримувати всі відгуки за заданим customer_id
SELECT review FROM customers WHERE customer_id = 42;

// Отримувати користувачів(customer_id), які залишили більше ніж N відгуків на платформі і які також залишили відгук для продукту product_id (N та product_id повинне задаватися в запиті)
//

// Дізнатися скільки позитивних відгуків (4 або 5 зірок) залишив вказаний користувач customer_id
SELECT COUNT(*) FROM customers WHERE customer_id = 42 AND star_rating > 3);
