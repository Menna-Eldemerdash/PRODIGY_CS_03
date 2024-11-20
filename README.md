# PRODIGY_CS_03
This Python script evaluates the strength of a password entered by the user. It checks for various password security criteria and provides feedback to help users create stronger passwords.

Features
Password Evaluation:

Checks if the password meets specific security criteria (length, uppercase, lowercase, numbers, and special characters).
Rates the password strength on a scale of 0–5:
5: Very strong password.
3 or 4: Moderate password.
Less than 3: Weak password.
Feedback System:

Provides clear feedback on why the password is weak and suggests improvements.
Interactive Design:

Allows users to re-enter a password until it meets the strength requirements.
How the Code Works
1. Imports
The script uses the re module for regex-based pattern matching to evaluate the password's structure.
2. Password Strength Function
The function check_password(password) performs the following checks:

Length:
Ensures the password is at least 8 characters long.
Adds 1 point to the strength variable if the condition is met.
Provides feedback if the password is too short.
Uppercase Letter:
Checks if the password contains at least one uppercase letter.
Adds 1 point if true; otherwise, feedback is given.
Lowercase Letter:
Checks for at least one lowercase letter.
Adds 1 point if true; otherwise, feedback is given.
Numeric Character:
Verifies that the password has at least one digit.
Adds 1 point if true; otherwise, feedback is given.
Special Character:
Ensures the presence of at least one special character (e.g., @, #, $).
Adds 1 point if true; otherwise, feedback is given.
The function returns:

strength: A numeric value representing the strength score (0–5).
feedback: A list of feedback messages highlighting missing elements.
3. Main Loop
The script runs interactively, allowing the user to test multiple passwords:

Prompts the user to enter a password.
Calls the check_password() function to evaluate its strength.
Displays:
A message about the password strength (Very Strong, Moderate, or Very Weak).
A detailed list of feedback if the password needs improvement.
Asks the user to re-enter the password if it isn't strong enough.
4. Termination
If the password meets all criteria (strength score = 5), the script exits with a "Password is very strong" message.
Example Usage
Input:
mathematica
Copy code
Enter your Password: pass123
Output:
vbnet
Copy code
Password is moderate. Try to make it stronger.
Password strength: 3
Password should contain at least one uppercase letter.
Password should contain at least one special character (@, #, $).

Please try again.
How to Run
Save the script as password_checker.py.
Run the script in your terminal or IDE:
Copy code
python password_checker.py
Enter a password and follow the feedback to create a strong password.
