Django Authentication/Authentication

## Basic Django Default Authentication

In this project, we are using Django's default authentication system. This is the easiest way to add login, logout, and user registration in our website. Django already gives us everything ready-made, so we don't need to write much code for user authentication.

### How it works

1. **User Model:** Django has a built-in User model. we can use it to create users, check passwords, and manage user info.
2. **Login & Logout:** Django gives us ready views and forms for login and logout. we just need to connect them in our urls.py.
3. **Admin Panel:** we can create users and manage them from Django admin panel also.

### Steps to use Default Authentication

1. **Add 'django.contrib.auth' and 'django.contrib.contenttypes' in our `INSTALLED_APPS` (already added by default).**
2. **Run migrations:**
	```bash
	python manage.py migrate
	```
3. **Create a superuser (admin):**
	```bash
	python manage.py createsuperuser
	```
4. **Login/Logout URLs:**
	we can use Django's built-in views for login and logout. Add these in our `urls.py`:
	```python
	from django.contrib.auth import views as auth_views

	urlpatterns = [
		 # ...existing urls...
		 path('login/', auth_views.LoginView.as_view(), name='login'),
		 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	]
	```
5. **Templates:**
	Create `registration/login.html` template for login page. Django will look for this file automatically.

### Example Login Template (registration/login.html)
```html
<h2>Login</h2>
<form method="post">
	 {% csrf_token %}
	 {{ form.as_p }}
	 <button type="submit">Login</button>
</form>
```

That's it! Now we can login and logout using Django's default system. If we want to add registration or customize, we can do that too. If we need help, just ask!
