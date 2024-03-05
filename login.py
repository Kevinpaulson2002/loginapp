import streamlit as st

def main():
    st.title("Login Page")

    # Input fields for username and password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login button
    if st.button("Login"):
        # Replace the following authentication logic with your own
        if authenticate(username, password):
            st.success("Login successful! Redirecting to the main app...")
            # You can add redirection logic or switch to another page here
        else:
            st.error("Authentication failed. Please check your credentials.")

def authenticate(username, password):
    # Replace this with your actual authentication logic
    return username == "user" and password == "password"

if __name__ == "__main__":
    main()
