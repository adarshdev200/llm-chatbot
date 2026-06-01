from conversation import Conversation



class ChatBot:
    def __init__(self, provider,database, system_prompt="",title="New Chat",):
        self.provider = provider
        self.conversation = Conversation(system_prompt=system_prompt)
        self.db = database

        self.conversation_id = self.db.create_conversation(title, system_prompt)
    
    def chat(self, user_input):
        self.conversation.add_user_message(user_input)
        self.db.save_message(self.conversation_id,"user",user_input)
        messages = self.conversation.to_api_format()
        response = self.provider.generate(messages)
        self.db.save_message(self.conversation_id,"assistant",response)
        
        # TODO 10: Return the response
        return response
    
    def show_history(self):
        for msg in self.conversation.messages:
            time_str = msg.timestamp.strftime("%H:%M")
            print(f"[{msg.role} @ {time_str}]: {msg.content}")
    
    def reset(self):
        self.conversation.clear()


    def load_conversation(self, conversation_id):

    # TODO 4: Fetch messages from the database

        new_convo = self.db.get_conversation_messages(conversation_id)
    
    # TODO 5: Clear the current in-memory conversation
        self.conversation.clear()
    
    # TODO 6: Update self.conversation_id to the loaded one

        self.conversation_id = conversation_id
        

    
    # TODO 7: Loop through the fetched messages and re-add them
        for row in new_convo:
            role = row[4]
            content = row[3]
            if role == "user":
                self.conversation.add_user_message(content)
            elif role == "assistant":
                self.conversation.add_assistant_message(content)
