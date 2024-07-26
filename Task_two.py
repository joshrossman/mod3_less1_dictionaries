#2. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use 
# nested collections and loops by creating a system to track customer service tickets.
#Problem Statement: Develop a program that:
#Tracks customer service tickets, each with a unique ID, customer name, 
# issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
ticket_number=3
def open_new_ticket():
    global ticket_number
    while True:
        new_customer=input("Customer's name:")
        issue=input("Customer's issue:")
        if ticket_number<10:
            new_key="Ticket00"+str(ticket_number)
        elif ticket_number<100:
            new_key="Ticket0"+str(ticket_number)
        elif ticket_number<100:
            new_key="Ticket"+str(ticket_number)
        else:
            print("Ticket Max Reached!")
            break
        ticket_number+=1
        new_ticket={new_key:{"Customer":new_customer,"Issue":issue,"Status":"Open"}}
        service_tickets.update(new_ticket)
        print(f"New ticket created: {new_ticket}")
        break
def update_status():
    print(service_tickets)
    new_status=''
    
    while True:   
        status_holder=input("Which status would you like to change? Input Ticket Number:")
        if status_holder.lower()=="menu":
            break
        try:
            if service_tickets[status_holder]["Status"].lower()=="open":           
                new_status="Closed"
            elif service_tickets[status_holder]["Status"].lower()=="closed":              
                new_status="Open" 
            service_tickets[status_holder]["Status"]=new_status
            print(f"Status of {status_holder} changed to {new_status}.")  
            break 
        except:
            print("Error! This ticket does not exsist!")
            print("Please enter a valid ticket - or type MENU to return to main menu.")
            
 
def display_and_filter():
    while True:
            my_printing_choice=input("What would you like to view?\n[1]Open Tickets.\n[2]Closed Tickets.\n[3]All Tickets\n")
            if my_printing_choice=="1" or my_printing_choice.lower()=="open" or my_printing_choice.lower()=="open tickets" :
                for value in service_tickets:
                    if service_tickets[value]["Status"].lower()=="open":
                        print(value,"\n", service_tickets[value])
            elif my_printing_choice=="2" or my_printing_choice.lower()=="closed" or my_printing_choice.lower()=="closed tickets" :
                for value in service_tickets:
                    if service_tickets[value]["Status"].lower()=="closed":
                        print(value,"\n", service_tickets[value])
            elif my_printing_choice=="3" or my_printing_choice.lower()=="all" or my_printing_choice.lower()=="all tickets" :
                for value in service_tickets:
                    print(value,"\n", service_tickets[value])
            break

while True:
    my_choice=input("Welcome! Please choose an option: \n[1]Open a new ticket.\n[2]Update a new ticket.\n[3]View tickets\n")
    if my_choice=="1" or my_choice.lower()=="open":
        open_new_ticket()
    elif my_choice=="2" or my_choice.lower()=="update":
        update_status()
    elif my_choice=="3" or my_choice.lower()=="view":
        display_and_filter()
    else:
        print("Invalid input! Please enter a number from 1 to 3")
        
