from flask import jsonify
import re
#validation of password requirements
def validate_password_strength(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search("[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search("[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search("[0-9]", password):
        return False, "Password must contain at least one digit"
    if not re.search("[!@#$%^&*()_+=-]", password):
        return False, "Password must contain at least one special character (!@#$%^&*()_+=-)"
    return True, "Password is strong"
#validation of login data
def validateLoginData( username, password):
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
        return {"error": "Username is not valid-Please enter a valid username-Eg:abc@gmail.com"}
    if not password:
        return jsonify({"error": "Password is required"}), 400
#validation for manager registration    
def validateRegisterData(fullname, username, password):
    if not fullname:
        return jsonify({"error": "Full name is required"}), 400
    if len(fullname) < 3:
        return jsonify({"error": "Full name must be at least 3 characters"}), 400
    if not all(i.isalpha() or i.isspace() for i in fullname):
        return jsonify({"error": "Full name can only contain letters and spaces"}), 400
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", username):
        return {"error": "Username is not valid-Please enter a valid username-Eg:abc@gmail.com"}
    if not password:
        return jsonify({"error": "Password is required"}), 400
    password_is_strong, password_error = validate_password_strength(password)
    if not password_is_strong:
        return jsonify({"error": password_error}), 400
    return None
#validation of employee data
def validateEmployeeData(name, skills,designation,project):
    if not name:
        return jsonify({"error": "name is required"}), 400
    if not skills:
        return jsonify({"error": "skills is required"}), 400
    if not designation:
        return jsonify({"error": "designation_id is required"}), 400
    if not project:
        return jsonify({"error": "project is required"}), 400
#validation of project data
def validateProjectData(name,start_date,department,manager):
    if not name:
        return jsonify({"error": "name is required"}), 400
    if not start_date:
        return jsonify({"error": "start_date is required"}), 400
    if not department:
        return jsonify({"error": "department is required"}), 400 
    if not manager:
        return jsonify({"error": "manager is required"}), 400       