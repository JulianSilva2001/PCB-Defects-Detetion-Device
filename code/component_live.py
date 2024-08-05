import streamlit as st

# Define your sidebar content
def sidebar_content():
    st.write("This is some sidebar content.")

# Set up Streamlit app
def main():
    # Add a background image to the sidebar using custom CSS
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: url("http://www.technocrazed.com/wp-content/uploads/2015/12/beautiful-wallpaper-download-13.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display sidebar content
    sidebar_content()

    # Main content
    st.write("This is the main content.")

if __name__ == "__main__":
    main()