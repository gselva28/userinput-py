name = input("Enter your name:")
surname = input("Enter your surname:")
when = "today"

message = "Hello %s %s" % (name, surname)
message1 = f"Hello {name} {surname}, What's up {when}"
print(message)
print(message1) 