import streamlit as st
import csv
import os

CSV_FILE = "users.csv"

# --- Initialization ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None


# --- Utility Functions ---
def load_users():
    """Load users from CSV into a dictionary"""
    users = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users[row["username"]] = row["password"]
    return users


def authenticate(username, password):
    users = load_users()
    return username in users and users[username] == password


def add_user(username, password):
    """Add new user to CSV"""
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "password"])
        writer.writerow([username, password])


def login(username, password):
    if authenticate(username, password):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.rerun()
    else:
        st.error("Invalid username or password")


def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.success("Logged out successfully")
    st.rerun()


# --- UI ---
st.title("Login System")

if not st.session_state.logged_in:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

    st.divider()
    st.subheader("Register(If not done)")

    new_user = st.text_input("New Username")
    new_pass = st.text_input("New Password", type="password")

    if st.button("Register"):
        add_user(new_user, new_pass)
        st.success("User registered successfully!")

else:
    st.success(f"Welcome, {st.session_state.username} 👋")
    if st.button("Logout"):
        logout()