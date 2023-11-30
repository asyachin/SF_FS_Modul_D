document.addEventListener("DOMContentLoaded", function() {

	var subscriptionLink = document.getElementById("subscription-link");
	if (subscriptionLink) {
			subscriptionLink.addEventListener("click", function(e) {
					e.preventDefault();
					var categoryId = this.getAttribute("data-category-id");
					var isSubscribed = this.getAttribute("data-subscribed") === "true";
					var url = isSubscribed ? "/unsubscribe/" + categoryId + "/" : "/subscribe/" + categoryId + "/";
					fetch(url, {
							method: 'POST',
							headers: {
									'X-CSRFToken': getCookie('csrftoken'),  // Получение CSRF токена
									'Content-Type': 'application/json',
							},
					})
					.then(response => response.json())
					.then(data => {
							if(data.status === 'subscribed' || data.status === 'unsubscribed') {
									this.textContent = isSubscribed ? "Подписаться" : "Отписаться";
									this.setAttribute("data-subscribed", !isSubscribed);
							}
					})
					.catch(error => console.error('Ошибка:', error));
			});
	}
});

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