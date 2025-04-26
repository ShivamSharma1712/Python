def create_database():
    # List to store all records
    database = []
    
    # Get the number of records to add
    n = int(input("Enter the number of records: "))
    
    # Loop to input records
    for i in range(n):
        print(f"\nEntering details for record {i + 1}:")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        subject = input("Enter Subject: ")
        
        # Create a tuple for the record
        record = (name, age, subject)
        
        # Add the tuple to the list
        database.append(record)
    
    return database

def display_database(database):
    print("\nDatabase Records:")
    print(f"{'Name':<20} {'Age':<5} {'Subject':<15}")
    print("-" * 40)
    for record in database:
        name, age, subject = record
        print(f"{name:<20} {age:<5} {subject:<15}")

# Main Program
database = create_database()
display_database(database)