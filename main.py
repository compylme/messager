person_A = input("person_A, please enter your name: " )
print("Your name is: " + person_A)
person_B = input("person_B, please enter your name: ")
print("Your name is: " + person_B)
print (person_A + " and " + person_B + ", " + "nice to meet you both!")

message_log = []
message_controller = 0
person_A_messages = []
person_B_messages = []
next_message = " "
message_id = 0
message_id_storage = []

while person_A == person_A  and person_B == person_B:
  identifier = input("Please enter your name: " + " ")
  next_message = input("Please enter the next message: ")
  next_message_and_identifier = identifier + ": " + next_message
  message_id += 1
  message_id_storage.append(message_id)
  if next_message != "end":
    message_log.append(next_message_and_identifier)
    
  
  if next_message == "end":
    print(message_log)
    print(len(message_log))
    print(message_id_storage)
    message_id_pairs = zip(message_id_storage, message_log)
    zipped_message_id_pairs = list(message_id_pairs)
    print(zipped_message_id_pairs)

