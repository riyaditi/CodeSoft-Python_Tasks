import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import messagebox, simpledialog


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        ttk.Label(self.root, text="Contact Book", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=3, pady=10)

        ttk.Label(self.root, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky='E')
        ttk.Entry(self.root, textvariable=self.name_var).grid(row=1, column=1, padx=5, pady=5, sticky='W')

        ttk.Label(self.root, text="Phone:").grid(row=2, column=0, padx=5, pady=5, sticky='E')
        ttk.Entry(self.root, textvariable=self.phone_var).grid(row=2, column=1, padx=5, pady=5, sticky='W')

        ttk.Label(self.root, text="Email:").grid(row=3, column=0, padx=5, pady=5, sticky='E')
        ttk.Entry(self.root, textvariable=self.email_var).grid(row=3, column=1, padx=5, pady=5, sticky='W')

        ttk.Label(self.root, text="Address:").grid(row=4, column=0, padx=5, pady=5, sticky='E')
        ttk.Entry(self.root, textvariable=self.address_var).grid(row=4, column=1, padx=5, pady=5, sticky='W')

        # Buttons
        ttk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=7, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=8, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_var.get().strip()

        if name and phone:
            contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.contacts.append(contact)
            messagebox.showinfo('Success', 'Contact added successfully!')
            self.clear_entries()
        else:
            messagebox.showwarning('Warning', 'Name and Phone are required fields.')

    def view_contacts(self):
        if self.contacts:
            view_window = tk.Toplevel(self.root)
            view_window.title('Contact List')

            for i, contact in enumerate(self.contacts, start=1):
                contact_str = f"{i}. {contact['Name']} - {contact['Phone']}"
                ttk.Label(view_window, text=contact_str).pack(pady=5)
        else:
            messagebox.showinfo('Information', 'No contacts available.')

    def search_contact(self):
        search_str = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_str:
            result = [contact for contact in self.contacts if
                      search_str.lower() in contact['Name'].lower() or search_str in contact['Phone']]
            if result:
                search_window = tk.Toplevel(self.root)
                search_window.title('Search Result')

                for i, contact in enumerate(result, start=1):
                    contact_str = f"{i}. {contact['Name']} - {contact['Phone']}"
                    ttk.Label(search_window, text=contact_str).pack(pady=5)
            else:
                messagebox.showinfo('Information', 'No matching contacts found.')
        else:
            messagebox.showwarning('Warning', 'Please enter a search term.')

    def update_contact(self):
        search_str = simpledialog.askstring("Update", "Enter name or phone number:")
        if search_str:
            result = [contact for contact in self.contacts if
                      search_str.lower() in contact['Name'].lower() or search_str in contact['Phone']]
            if result:
                selected_contact = result[0]
                update_window = tk.Toplevel(self.root)
                update_window.title('Update Contact')

                ttk.Label(update_window, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='E')
                ttk.Entry(update_window, textvariable=self.name_var).grid(row=0, column=1, padx=5, pady=5, sticky='W')
                self.name_var.set(selected_contact['Name'])

                ttk.Label(update_window, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky='E')
                ttk.Entry(update_window, textvariable=self.phone_var).grid(row=1, column=1, padx=5, pady=5, sticky='W')
                self.phone_var.set(selected_contact['Phone'])

                ttk.Label(update_window, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky='E')
                ttk.Entry(update_window, textvariable=self.email_var).grid(row=2, column=1, padx=5, pady=5, sticky='W')
                self.email_var.set(selected_contact['Email'])

                ttk.Label(update_window, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky='E')
                ttk.Entry(update_window, textvariable=self.address_var).grid(row=3, column=1, padx=5, pady=5, sticky='W')
                self.address_var.set(selected_contact['Address'])

                ttk.Button(update_window, text="Update", command=lambda: self.perform_update(update_window, selected_contact)).grid(
                    row=4, column=0, columnspan=2, pady=10)
            else:
                messagebox.showinfo('Information', 'No matching contacts found.')
        else:
            messagebox.showwarning('Warning', 'Please enter a search term.')

    def perform_update(self, update_window, selected_contact):
        updated_name = self.name_var.get().strip()
        updated_phone = self.phone_var.get().strip()
        updated_email = self.email_var.get().strip()
        updated_address = self.address_var.get().strip()

        if updated_name and updated_phone:
            selected_contact['Name'] = updated_name
            selected_contact['Phone'] = updated_phone
            selected_contact['Email'] = updated_email
            selected_contact['Address'] = updated_address

            messagebox.showinfo('Success', 'Contact updated successfully!')
            update_window.destroy()
            self.clear_entries()
        else:
            messagebox.showwarning('Warning', 'Name and Phone are required fields.')

    def delete_contact(self):
        search_str = simpledialog.askstring("Delete", "Enter name or phone number:")
        if search_str:
            result = [contact for contact in self.contacts if
                      search_str.lower() in contact['Name'].lower() or search_str in contact['Phone']]
            if result:
                confirmation = messagebox.askyesno('Confirmation', 'Are you sure you want to delete this contact?')
                if confirmation:
                    self.contacts.remove(result[0])
                    messagebox.showinfo('Success', 'Contact deleted successfully!')
            else:
                messagebox.showinfo('Information', 'No matching contacts found.')
        else:
            messagebox.showwarning('Warning', 'Please enter a search term.')

    def clear_entries(self):
        self.name_var.set('')
        self.phone_var.set('')
        self.email_var.set('')
        self.address_var.set()

if __name__ == "__main__":
    root = tk.Tk()

    # Styling
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5)

    contact_book = ContactBook(root)

    # Run the Tkinter event loop
    root.mainloop()