data = [{"id" : "ID123", "name :" "Janu" "age": 27}]
identification_number = "ID123"
person = next((item for item in data if item["id"] == identification_number), "ID not found")
print(person)
