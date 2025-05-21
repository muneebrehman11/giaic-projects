import streamlit as st
import json
import os

# File to save/load library data
FILE_NAME = "library_data.json"

# Load library data from file if exists
def load_library():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    else:
        return []

# Save library data to file
def save_library(library):
    with open(FILE_NAME, "w") as f:
        json.dump(library, f, indent=4)

# Add a book
def add_book(library, book):
    library.append(book)
    save_library(library)

# Remove book by title (case insensitive)
def remove_book(library, title):
    before_count = len(library)
    library[:] = [b for b in library if b['title'].lower() != title.lower()]
    save_library(library)
    return len(library) < before_count

# Search books by title or author substring
def search_books(library, query):
    query = query.lower()
    return [b for b in library if query in b['title'].lower() or query in b['author'].lower()]

# Display books nicely
def display_books(books):
    for i, b in enumerate(books, 1):
        st.write(f"### {i}. {b['title']}")
        st.write(f"- Author: {b['author']}")
        st.write(f"- Year: {b['year']}")
        st.write(f"- Genre: {b['genre']}")
        st.write(f"- Read: {'✅ Yes' if b['read'] else '❌ No'}")
        st.write("---")

# Calculate stats
def get_stats(library):
    total = len(library)
    read_count = sum(1 for b in library if b['read'])
    read_percent = (read_count / total * 100) if total > 0 else 0
    return total, read_percent

# --- Streamlit UI starts here ---
st.title("📚 Personal Library Manager")

library = load_library()

menu = st.sidebar.selectbox("Menu", ["Add Book", "Remove Book", "Search Books", "Display All Books", "Statistics", "Exit"])

if menu == "Add Book":
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        if not title or not author:
            st.error("Please enter at least Title and Author.")
        else:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read
            }
            add_book(library, book)
            st.success(f"Book '{title}' added!")

elif menu == "Remove Book":
    st.header("Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove"):
        if remove_book(library, title):
            st.success(f"Book '{title}' removed.")
        else:
            st.warning(f"No book found with title '{title}'.")

elif menu == "Search Books":
    st.header("Search Books")
    query = st.text_input("Enter title or author to search")
    if query:
        results = search_books(library, query)
        if results:
            st.write(f"Found {len(results)} book(s):")
            display_books(results)
        else:
            st.warning("No matching books found.")

elif menu == "Display All Books":
    st.header("All Books in Library")
    if library:
        display_books(library)
    else:
        st.info("No books in library yet.")

elif menu == "Statistics":
    st.header("Library Statistics")
    total, read_percent = get_stats(library)
    st.write(f"Total books: {total}")
    st.write(f"Percentage read: {read_percent:.2f}%")

elif menu == "Exit":
    st.write("Thank you for using Personal Library Manager! Close the tab to exit.")

