import smtplib
import tkinter as tk
from tkinter import messagebox

def send_email():
    """Send an email using SMTP."""
    sender_email = entry_sender.get()
    recipient_email = entry_recipient.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)

    if not sender_email or not recipient_email or not subject or not body.strip():
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return

    try:
        # Set up the server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, entry_password.get())
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

# Set up the main window
root = tk.Tk()
root.title("Email Sender")

# Set the background color
root.configure(bg="#f0f0f0")

# Create labels and entry fields
label_sender = tk.Label(root, text="Your Email:", bg="#f0f0f0")
label_sender.pack(pady=5)
entry_sender = tk.Entry(root, width=40)
entry_sender.pack(pady=5)

label_password = tk.Label(root, text="Password:", bg="#f0f0f0")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*", width=40)
entry_password.pack(pady=5)

label_recipient = tk.Label(root, text="Recipient Email:", bg="#f0f0f0")
label_recipient.pack(pady=5)
entry_recipient = tk.Entry(root, width=40)
entry_recipient.pack(pady=5)

label_subject = tk.Label(root, text="Subject:", bg="#f0f0f0")
label_subject.pack(pady=5)
entry_subject = tk.Entry(root, width=40)
entry_subject.pack(pady=5)

label_body = tk.Label(root, text="Body:", bg="#f0f0f0")
label_body.pack(pady=5)
text_body = tk.Text(root, height=10, width=40)
text_body.pack(pady=5)

# Create a button to send the email
send_button = tk.Button(root, text="Send Email", command=send_email, bg="#4CAF50", fg="white")
send_button.pack(pady=20)

# Start the main event loop
root.mainloop()