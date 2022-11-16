from testing import Testing

obj = Testing()

while True:
    query = input("Ask me anything..  ")
    if query=="exit":
        print("Good Bye")
        break
    else:
        ans = obj.response(query)
        print("Bot Reply: ",ans)
