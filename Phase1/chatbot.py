import nltk
from nltk.chat.util import Chat, reflections

# Download the required NLTK data files
nltk.download('punkt')

# Define pairs of input patterns and corresponding responses
pairs = [
    [
        r"(hi|hello|hey|good morning|good evening|good afternoon)",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"schedule a task (.*)",
        ["I have scheduled the task: '%1'. What else would you like to do?", 
         "Task '%1' has been scheduled successfully."]
    ],
    [
        r"(.*)(schedule|set|add) (.*) for (.*)",
        ["I have added '%3' to your schedule for %4.", 
         "Task '%3' is scheduled for %4."]
    ],
    [
        r"what's on my schedule(.*)",
        ["You have these tasks scheduled: %1", 
         "Here are your scheduled tasks: %1."]
    ],
    [
        r"(thank you|thanks|thanks a lot)",
        ["You're welcome! Happy to help.", "No problem! Let me know if you need anything else."]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day ahead.", "Bye! Take care."]
    ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Start the chatbot conversation
def start_chatbot():
    print("Hello! I am your assistant. How can I help you today?")
    chatbot.converse()

if __name__ == "__main__":
    start_chatbot()
