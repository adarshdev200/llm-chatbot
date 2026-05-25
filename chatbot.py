from conversation import Conversation


class ChatBot:
    def __init__(self, provider, system_prompt=""):
        self.provider = provider
        self.conversation = Conversation(system_prompt=system_prompt)
    
    def chat(self, user_input):
        # TODO 7: Add user message to conversation

        self.conversation.add_user_message(user_input)

        
        # TODO 8: Send the FULL conversation (with history!) to the provider
        #   Hint: use self.conversation.to_api_format()
        #   This is critical — it's what makes the bot remember context

        messages = self.conversation.to_api_format()
        
        # TODO 9: Get response and add it as an assistant message

        response = self.provider.generate(messages)
        
        # TODO 10: Return the response
        return response
    
    def show_history(self):
        for msg in self.conversation.messages:
            time_str = msg.timestamp.strftime("%H:%M")
            print(f"[{msg.role} @ {time_str}]: {msg.content}")
    
    def reset(self):
        self.conversation.clear()
    