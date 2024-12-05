import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

class ChatBotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Jarvis 2.0")

        # Create ChatBot instance
        pairs = [
            [
                r"my name is (.*)",
                ["Hello %1, how can I help you today?",]
            ],
            [
                r"hello",
                ["Hello my name is Jarvis 2.0",]
            ],[
                r"How was your day?",
                ["My day was great.",]
            ],
            [
                r"what is your name?",
                ["My name is Jarvis 2.0 and I'm here to assist you.",]
            ],
            [
                r"how are you ?",
                ["I'm doing well, thank you!",]
            ],
            [
                r"sorry (.*)",
                ["No need to apologize, it's alright.",]
            ],
            [
                r"quit",
                ["Bye! Take care. :)",]
            ],]
        self.chatbot = Chat(pairs, reflections)

        # Create GUI elements
        self.output = scrolledtext.ScrolledText(master, width=50, height=20, state='disabled')
        self.output.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_label = tk.Label(master, text="User Input:")
        self.input_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')

        self.input_entry = tk.Entry(master, width=30)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def send_message(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, 'end')
        self.output.config(state='normal')
        self.output.insert(tk.END, "You: " + user_input + "\n")
        response = self.chatbot.respond(user_input)
        self.output.insert(tk.END, "Jarvis 2.0: " + response + "\n")
        self.output.see(tk.END)
        self.output.config(state='disabled')

def main():
    root = tk.Tk()
    chatbot_gui = ChatBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()