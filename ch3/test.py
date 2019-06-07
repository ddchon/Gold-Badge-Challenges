event1 = (1000, "golf")
event2 = (1000, "park")
event3 = (1500, "golf")

event_list = [event1, event2, event3]

total = 0
for i in event_list:
    if i[1] == "golf":
        total += i[0]

print(total)


# print(sum(event_list[0]))