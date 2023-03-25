# Lead model implimetaion

# Define the lead data that you want to create
lead_data = {
    "LastName": "Doe",
    "FirstName": "John",
    "Company": "Acme Inc.",
    "Email": "jdoe@acme.com"
}

# Send a POST request to create the lead
response = requests.post(url, headers=headers, data=json.dumps(lead_data))

# Check if the request was successful
if response.status_code == 201:
    print("Lead created successfully")
else:
    print("Failed to create lead. Status code:", response.status_code)