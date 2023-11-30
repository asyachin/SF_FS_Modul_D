function addCategory() {
	var select = document.getElementById('add_category');
	var categoryId = select.value;
	var articleId = select.getAttribute('article_id');
	
	// Создаем URL для запроса
	var url = '/news/' + articleId + '/edit/' + categoryId;

	// Отправляем запрос
	fetch(url, {
			method: 'POST',
			headers: {
					'X-CSRFToken': getCookie('csrftoken'),  // Передаем CSRF токен
					'Content-Type': 'application/json'
			},
			body: JSON.stringify({ 'categoryId': categoryId })
	})
	.then(response => response.json())
	.then(data => {
			console.log('Success:', data);
			// Действия после успешного запроса (например, обновление страницы)
	})
	.catch((error) => {
			console.error('Error:', error);
	});
}

// Функция для получения CSRF токена
function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
			const cookies = document.cookie.split(';');
			for (let i = 0; i < cookies.length; i++) {
					const cookie = cookies[i].trim();
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
					}
			}
	}
	return cookieValue;
}
