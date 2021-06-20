# Follow the instructions for how to code this application

print("Enter a guest's name or type 'end' to stop.")

cost_per_guest = 12

guest_input = input()
guest_list = []
while guest_input.lower() != "end":
    guest_list.append(guest_input)
    guest_input = input("Enter a guest's name or type 'end' to stop.\n")

total_guests = len(guest_list)
guest_total_cost = total_guests * cost_per_guest


print(
    f"You have invited {total_guests} guests at a cost of ${guest_total_cost:.2f}")
