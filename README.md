# Django_Delete_Confirmation_with_Bulma

[referred blog](https://narito.ninja/blog/detail/119/)


[How_to_use_Bulma_1](https://pypi.org/project/django-simple-bulma/)


[How_to_use_Bulma_2](https://github.com/timonweb/django-bulma)

![Delete-Confirmation-with-Bulma](Delete-Confirmation-with-Bulma.gif)

> ## models.py
``` python
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.title
```

> ## admin.py
``` python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

> ## views.py
``` python
from django.urls import reverse_lazy
from .models import Post
from django.views import generic


class PostIndex(generic.ListView):
    model = Post

class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('app:post_list')
```

> ## urls.py
``` python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostIndex.as_view(), name='post_list'),
    path('/delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),   
]
```

> ## base.html
``` python
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
</head>
<body>
{% block content %}{% endblock %}
{% block extrajs %}{% endblock %}
</body>
</html>
```

> ## post_list.html
``` python
{% extends 'app/base.html' %}

{% block content %}
    <section class="section">
        <div class="container">
            <h1 class="title">Post List</h1>
            {% for post in post_list %}
                <div class="box">
                    <div class="columns">
                        <div class="column is-11">
                            <h2>{{ post.title }}</h2>
                        </div>
                        <div class="column is-1">
                            <button type="button" class="button is-danger delete-modal-button" data-deleteurl="{% url 'app:post_delete' post.pk %}">Delete</button>
                        </div>
                    </div>
                </div>

            {% endfor %}
        </div>
    </section>

    <div class="modal" id="modal">
        <div class="modal-background"></div>
        <div class="modal-card">
            <header class="modal-card-head">
                <p class="modal-card-title">Confirm</p>
            </header>
            <section class="modal-card-body">
                Are you sure to delete this item?
            </section>
            <footer class="modal-card-foot">
                <form action="" method="POST" id="delete-form">
                    {% csrf_token %}
                    <button type="button" class="button is-info" id="delete-cancel-button">Cancel</button>
                    <button type="submit" class="button is-danger">Delete</button>
                </form>
            </footer>
        </div>
    </div>

{% endblock %}

{% block extrajs %}
    <script>
        const deleteForm = document.getElementById('delete-form');
        const modal = document.getElementById('modal');
        const deleteCancelButton = document.getElementById('delete-cancel-button');
        const deleteModalButtons = document.getElementsByClassName('delete-modal-button');

        for (const button of deleteModalButtons) {
            button.addEventListener('click', () => {
                modal.classList.add('is-active');
                deleteForm.action = button.dataset.deleteurl;
            });
        }

        deleteCancelButton.addEventListener('click', () => {
            modal.classList.remove('is-active');
        });
    </script>
{% endblock %}
```
