# Simple-Login-System

# Member's names
>>Jinesh S Parmar PES1UG25CS623 C11,
>>Gyanendra Kumar PES1UG25CS195 C11,
>>Kalmesh B PES1UG25CS240 C11,
>>Chinmay K PES1UG25CS144 C11,
                         
# Problem statement
>>To develop a simple, file-based, web application that allows users to register new accounts and log in securely. The system must persist user credentials (username and password) by storing them in a local CSV file, providing a basic, yet functional, demonstration of user authentication and session management in a web context using Python's Streamlit framework.
                        
# Methodology 
The application follows a client-server/web-based approach using Streamlit for the frontend and Python's built-in modules for backend logic and data handling.
>Session Management: The core of the login state is maintained using st.session_state (lines 10-14). The keys logged_in and username track the user's current authentication status.

​>File Handling: The built-in csv module is used to read and write user data from the users.csv file (lines 20-43).

​>User Interface: Streamlit components like st.title, st.subheader, st.text_input, and st.button are used to build the interactive login and registration forms (lines 72-97).
                     
# Data strutures used 
>>CSV File (users.csv): The primary persistent storage, acting as a simple database. It stores user credentials in a structured, comma-separated format with two columns: username and password.

​>>Python Dictionary (users in load_users function): Used in memory to efficiently store and retrieve credentials during the authentication check. The username acts as the key, and the password is the value (lines 21-28).
                    
# Kea functions and logic flow 
>>Load_users() (lines 19-28): Reads users.csv and populates the in-memory dictionary for quick lookups.

​>>Authenticate() (lines 31-33): Compares the provided username and password against the data loaded from the CSV.

​>>Add_user() (lines 36-43): Appends new user credentials to the users.csv file. It also ensures the header row is written only once if the file is created for the first time.
                    
# Sample Input/Output

>>​Sample Input (Registration)

​New Username: jackfruit_lover

​New Password: project@123

>>​Sample Output (CSV File)
​After registration, the users.csv file would contain a new entry:
username,password
jackfruit_lover,project@123
>Sample Output (Login Success)

​Input: Existing username and correct password.

​Output (Screen): A success message is displayed: Welcome, [username] 👋 (line 89).
                 
# Challenges Faced
​>>Streamlit Reruns: Ensuring the Streamlit application reruns correctly upon state change (login/logout) to update the UI without manual intervention. This was addressed by using st.rerun() within the login and logout functions (lines 53 and 64).

​>>Initial File Handling: Ensuring the users.csv file and its header row are correctly created the first time the application is run, without overwriting existing data on subsequent runs. This was handled by checking os.path.exists(CSV_FILE) (lines 37 and 39).

​>>Security (Weakness): The current system stores passwords in plaintext within the CSV file, which is a significant security risk.
                
# Scope for Improvement

​>>Password Hashing: Implement robust security by using a cryptographic hashing library (e.g., bcrypt) to store and compare hashed passwords instead of plaintext.

​>>Database Integration: Replace the basic CSV file with a proper database (like SQLite, MySQL, or PostgreSQL) for more scalable and transactional data management.

​>>Input Validation: Add checks to ensure usernames are unique and passwords meet minimum complexity requirements (length, special characters).

​>>Error Handling: Implement try...except blocks for file operations to gracefully handle potential I/O errors (e.g., file not found, permission issues).


