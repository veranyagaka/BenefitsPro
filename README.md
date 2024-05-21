Bullet points
- [x] Login Redirection
- [ ] Migrations, Database, Models
- [ ] Application requests + Applications table (therefore also the html page)
- [ ] Admin - approval of applications and update the benefits provided by the company
- [ ] Log out page
- [ ] Sessions/ Timeouts to be implemented
- [ ] Profile page - settings to change password & other preferences
- [ ] Profile page: Dependents, Benefitiaries (this means more tables)
- [ ] View the reflection on the applications page
- [ ] Redirection to various pages + @login_required
- [ ] Forms.py
- [ ] Reset Password/ Forgot password
- [ ] Tables, tables,tables
- [ ] Better Error Handling
- [ ] CSS + Images
- [ ] Navigation on the profiles page: Broken links fix
- [ ] Deployment Finally and some little testing
# Group them in order / in modules
## lets start with links and navigation
## databases, models and migrations
## Benefits and Applications page!!!!!!
## Additional info later
## Testing to see every functionality works
## Display of info and its css one of the last


<!--For your Benefits Administration System project, here's a list of HTML files you might need:

index.html: Landing page or dashboard for the system.
login.html: Login page for users.
signup.html: Signup page for new users.
profile.html: User profile page displaying employee information and benefits.
benefits.html: Page to manage employee benefits (add, edit, delete benefits).
enrollment.html: Page for employees to enroll in benefits.
admin.html: Admin dashboard for managing user accounts and benefits.
For the database schema, you might consider the following tables:

User: Store user information (id, username, password, email, etc.).
Employee: Store employee-specific information (employee_id, name, position, department, etc.).
Benefit: Store information about benefits (benefit_id, name, description, coverage, etc.).
Enrollment: Store information about benefit enrollments (enrollment_id, employee_id, benefit_id, enrollment_date, etc.).
Here's an example schema in SQL for PostgreSQL:

sql
Copy code
CREATE TABLE "User" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL
);

CREATE TABLE Employee (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES "User" (id),
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE Benefit (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    coverage VARCHAR(255)
);

CREATE TABLE Enrollment (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES Employee (id),
    benefit_id INTEGER REFERENCES Benefit (id),
    enrollment_date DATE NOT NULL
);
For displaying values on the profile page, you can use Django templates to render dynamic content. For example, to display a user's name and department on the profile page, you can pass the user's information to the template and render it like this:

html
Copy code
<h1>Welcome, {{ user.employee.name }}</h1>
<p>Department: {{ user.employee.department }}</p>
This assumes that you have a User model with a one-to-one relationship to an Employee model. Adjust the template according to your actual models and data structure.
## Dont forget to register your app here and in the installed apps in settings.py

from django.contrib import admin
from .models import YourModelName

admin.site.register(YourModelName)
-->
Analysis of files i actually need: 1. for users
- settings
- benefits applications page - view applications and stuff
- reset password
- 2. for admin
- approve, deny application
