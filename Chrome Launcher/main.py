import tkinter as tk
from tkinter import messagebox
import subprocess as wb
import sys

class AuthApp:
    # Class-level variable for preset valid users and their passwords
    valid_users = {
        "username": "password" # these are the lines you should change for the preset account
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Authentication System") # set any name you want
        self.root.geometry("400x300") # set any size you want
        root.iconbitmap('icon.ico') # set your actual icon, this is what I actually wrote for my April Fools
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)
        
        # Show login screen by default
        self.show_login_screen()

    def clear_frame(self):
        """Clear all widgets from the main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def on_login_success(self):
        """Function to run after successful login"""
        # Example application content
        tk.Button(self.main_frame, 
                text="Continue to Application", 
                command=self.your_application_function).pack()
        
        # Logout button
        tk.Button(self.main_frame,
                text="Logout",
                command=self.show_login_screen).pack(pady=10)
    
    def your_application_function(self):
        """Replace this with your actual application function"""
        messagebox.showinfo("Application", "This would launch your main application!")
    
    def show_login_screen(self):
        """Display the login screen"""
        self.clear_frame()
        
        # Title
        tk.Label(self.main_frame, text="Login", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Username
        tk.Label(self.main_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.login_username = tk.Entry(self.main_frame)
        self.login_username.grid(row=1, column=1, padx=5, pady=5)
        
        # Password
        tk.Label(self.main_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.login_password = tk.Entry(self.main_frame, show="*")
        self.login_password.grid(row=2, column=1, padx=5, pady=5)
        
        # Login button
        tk.Button(self.main_frame, text="Login", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)

        # Sign up link
        tk.Label(self.main_frame, text="Don't have an account?").grid(row=4, column=0, columnspan=2)
        self.signup_link = tk.Label(self.main_frame, text="Sign up here", fg="blue", cursor="hand2")
        self.signup_link.grid(row=5, column=0, columnspan=2)
        self.signup_link.bind("<Button-1>", lambda e: self.show_signup_screen())
    
    def show_signup_screen(self):
        """Display the sign up screen"""
        self.clear_frame()
        
        # Title
        tk.Label(self.main_frame, text="Sign Up", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Username
        tk.Label(self.main_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.signup_username = tk.Entry(self.main_frame)
        self.signup_username.grid(row=1, column=1, padx=5, pady=5)
        
        # Password
        tk.Label(self.main_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.signup_password = tk.Entry(self.main_frame, show="*")
        self.signup_password.grid(row=2, column=1, padx=5, pady=5)
        
        # Confirm Password
        tk.Label(self.main_frame, text="Confirm Password:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.signup_confirm = tk.Entry(self.main_frame, show="*")
        self.signup_confirm.grid(row=3, column=1, padx=5, pady=5)
        
        # Sign up button
        tk.Button(self.main_frame, text="Sign Up", command=self.signup).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Login link
        tk.Label(self.main_frame, text="Already have an account?").grid(row=5, column=0, columnspan=2)
        self.login_link = tk.Label(self.main_frame, text="Login here", fg="blue", cursor="hand2")
        self.login_link.grid(row=6, column=0, columnspan=2)
        self.login_link.bind("<Button-1>", lambda e: self.show_login_screen())
    
    def login(self):
        """Handle login attempt"""
        username = self.login_username.get()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        # Check if the username and password are in the valid users list or not
        if username in self.valid_users and self.valid_users[username] == password:
            wb.Popen(["start", "chrome", "--new-tab"], shell=True) # this example runs chrome, but you can choose whatever app or file you wanna open
            sys.exit()
            messagebox.showinfo("Success", "Login successful!")
            self.on_login_success()
        else:
            # Any failure returns the specified message
            messagebox.showerror("Error", "Account retrieving failed, try again later")
    
    def signup(self):
        """Handle sign up attempt"""
        username = self.signup_username.get()
        password = self.signup_password.get()
        confirm = self.signup_confirm.get()
        
        if not username or not password or not confirm:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords don't match")
            return
            
        if username in self.valid_users:
            messagebox.showerror("Error", "Username already exists")
            return
        
        self.valid_users[username] = password
        messagebox.showinfo("Success", "Account created successfully!")
        self.show_login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()
