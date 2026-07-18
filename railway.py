class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dispaly(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        
class passenger(person):
    def __init__(self,name,age,passenger_id):
        super().__init__(name,age)
        self.passenger_id = passenger_id
        
    def display(self):
        print("\n----- passenger details -----")
        print(f"passenger ID: {self.passenger_id}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        
class train:
    def __init__(self,train_no,train_name, source, destination):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        
    def display_train(self):
        print("train number :", self.train_no) 
        print("train name :", self.train_name)
        print("source :", self.source)
        print("destination :", self.destination)
        
        
class ticket:
    def __init__(self, ticket_id,passenger,train,fare):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.train = train
        self.fare = fare
        
    def print_ticket(self):
        print("\n==== TICKET ====")
        print("Ticket ID :", self.ticket_id)
        print("passenger:", self.passenger.name)
        print("train:", self.train.train_name)
        print("train number:", self.train.train_no)
        print("from:", self.train.source)
        print("to:", self.train.destination)
        print("fare:", self.fare)
        print("================")
        
        p = passenger("mounika", 21, "p101")
        t = train(12727,"godavari express", "hyderabad","visakhapatnam")
        tk = ticket("T1001", p, t, 650)
        
        
        p.display()
        t.display_train()
        tk.print_ticket()