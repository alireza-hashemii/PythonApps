import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Replace 'YOUR_API_KEY' with your actual TMDB API key
TMDB_API_KEY = '195054922fdb93f5794d09791df40d4e'
TMDB_API_URL = 'https://api.themoviedb.org/3/search/movie'

def fetch_movie_poster(movie_name):
    params = {
        'api_key': '195054922fdb93f5794d09791df40d4e',
        'query': movie_name
    }
    response = requests.get(TMDB_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            poster_path = data['results'][0]['poster_path']
            if poster_path:
                return f'https://image.tmdb.org/t/p/w500{poster_path}'
    return None

def show_poster():
    movie_name = entry.get()
    if not movie_name:
        messagebox.showwarning("Input Error", "Please enter a movie name.")
        return

    poster_url = fetch_movie_poster(movie_name)
    if poster_url:
        try:
            image_response = requests.get(poster_url)
            image = Image.open(io.BytesIO(image_response.content))
            image = image.resize((250, 375), Image.ANTIALIAS)  # Resize the image
            poster = ImageTk.PhotoImage(image)
            
            # Clear previous image
            label.config(image='', text='')  
            label.image = poster  # Keep a reference to avoid garbage collection
            label.config(image=poster)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load image: {e}")
    else:
        messagebox.showinfo("No Results", "No movie found with that name.")

# Create the main window
root = tk.Tk()
root.title("Movie Poster Finder")

# Create and place the input field and button
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

search_button = tk.Button(root, text="Search", command=show_poster)
search_button.pack(pady=10)

# Create a label to show the poster
label = tk.Label(root)
label.pack(pady=20)

# Run the application
root.mainloop()