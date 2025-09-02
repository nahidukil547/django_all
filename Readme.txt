## 🔑 Purpose of the Authentication System in Django

The **Django authentication system** is designed to answer two key questions in a secure and structured way:

- **Who are you?** (Authentication)  
- **What are you allowed to do?** (Authorization)  

When building web applications such as an e-commerce site, a student management system, or a blog, we always need to:

- Identify users (login, signup)  
- Verify users (check password, email, tokens)  
- Control access (normal user vs. admin vs. staff)  
- Manage sessions (keep a user logged in until logout)  

Django provides all of these features out of the box, so developers don’t need to reinvent the wheel.

---

### 🎯 Main Purposes

1. **User Authentication (Identify user)**  
   - Verifies if the user is who they claim to be.  
   - Example: Login with username/email + password → Django validates using authentication backends → if correct, the user is authenticated.  

2. **User Authorization (Define permissions)**  
   - Determines what actions an authenticated user can perform.  
   - Example: An `is_staff` user can access the admin panel, but a normal user cannot.  

3. **Session Management**  
   - Keeps users logged in across multiple requests (using cookies + session ID).  
   - Example: You don’t need to log in again after every page reload.  

4. **Password & Security Handling**  
   - Stores passwords in a **hashed + salted** format (never plain text).  
   - Supports secure password change, reset, and recovery flows.  

5. **Pluggable Backends**  
   - Use the default authentication backend (username/password) or create custom ones (email login, phone OTP, JWT, etc.).  

6. **Integration with Django Admin**  
   - The same authentication system powers the Django admin interface.  
   - Makes it easy to manage users, groups, and permissions.  

---

### ⚡ Why It’s Important

- Saves development time with a secure, ready-made implementation.  
- Follows industry best practices (password hashing, CSRF protection, session security).  
- Flexible and extendable (custom authentication backends are supported).  
- Essential for any real-world project — from a small school project to a production-grade e-commerce platform.  


