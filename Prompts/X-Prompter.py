import os
import tkinter as tk
from tkinter import messagebox, filedialog
import markdown2
from tkhtmlview import HTMLLabel

__version__ = "0.2"  # Updated version number

def read_markdown_file(filename):
    """Read and return content from a markdown file."""
    if not os.path.exists(filename):
        messagebox.showerror("Error", f"File '{filename}' does not exist.")
        return None

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def display_markdown_content(content):
    """Display the rendered markdown content in an HTMLLabel widget."""
    window = tk.Toplevel()
    window.title("Markdown Content")

    # Render markdown to HTML
    html_content = markdown2.markdown(content)

    # Create an HTMLLabel to display the HTML content
    html_label = HTMLLabel(window, html=html_content)
    html_label.pack(padx=10, pady=10, fill="both", expand=True)

    # Add search functionality
    search_frame = tk.Frame(window)
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Search:")
    search_label.pack(side=tk.LEFT, padx=5)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)

    def search():
        search_term = search_entry.get().lower()
        if search_term:
            # Highlight search term in the HTML content
            highlighted_content = html_content.replace(
                search_term, f"<mark>{search_term}</mark>"
            )
            html_label.set_html(highlighted_content)

    search_button = tk.Button(search_frame, text="Search", command=search)
    search_button.pack(side=tk.LEFT, padx=5)

def open_file():
    """Open a file dialog to select a markdown file and display its content."""
    filename = filedialog.askopenfilename(
        title="Select a Markdown file",
        filetypes=(("Markdown files", "*.md"), ("All files", "*.*"))
    )
    if filename:
        content = read_markdown_file(filename)
        if content:
            display_markdown_content(content)

def main():
    # Create the main window
    root = tk.Tk()
    root.title(f"X-Prompter v{__version__}")

    # Create a button to open the file dialog
    open_button = tk.Button(root, text="Open Markdown File", command=open_file)
    open_button.pack(pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
