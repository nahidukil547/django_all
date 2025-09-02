## 🔑 Purpose of the Authentication System in Django

The **authentication system in Django** is there to handle **“Who are you?”** and **“What are you allowed to do?”** in a secure and structured way.

When we build any web app in Django – like an e-commerce site, a student management system, or a blog – we always need a way to:

* Identify users (login, signup)
* Verify users (check password, email, tokens)
* Control access (normal user vs admin vs staff)
* Manage sessions (keep user logged in until logout)

Django’s auth system already gives us these features out of the box, so we don’t have to code them from zero.

---

### 🎯 Main Purposes

1. **User Authentication (Identify user)**

   * Check if the user is who they say they are.
   * Example: You login with username/email + password → Django validates using backends → if ok, you’re authenticated.

2. **User Authorization (What can user do?)**

   * Once user is logged in, Django checks permissions/roles.
   * Example: An `is_staff` user can access admin panel, but a normal user cannot.

3. **Session Management**

   * Keeps the user logged in across multiple requests (using cookies + session ID).
   * Example: You don’t need to re-login on every page reload.

4. **Password & Security Handling**

   * Automatically stores passwords in **hashed + salted** form, never in plain text.
   * Supports password change, reset, and recovery flow.

5. **Pluggable Backends**

   * You can use the default auth backend (username/password), or write custom ones (login with email, phone, OTP, JWT).

6. **Integration with Django Admin**

   * The same authentication system powers the Django admin panel.
   * Easy to manage users, groups, and permissions.

---

### ⚡ Why It’s Important

* Saves development time (ready-made, secure implementation).
* Follows best practices (password hashing, CSRF protection, session security).
* Flexible (you can extend/replace parts if needed).
* Critical for **any real-world project** – whether it’s a school project or a production-level e-commerce app.

