class Property:
    def __init__(self, address, size, property_type):
        self.address = address
        self.size = size
        self.property_type = property_type

    def __str__(self):
        return f"{self.address}, {self.size} sqft, Type: {self.property_type}"

class Tenant:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def __str__(self):
        return f"{self.name}, Contact: {self.contact_info}"
        
class Lease:
    def __init__(self, property, tenant, start_date, end_date, rent):
        self.property = property
        self.tenant = tenant
        self.start_date = start_date
        self.end_date = end_date
        self.rent = rent

    def __str__(self):
        return f"Lease for {self.property.address}, Tenant: {self.tenant.name}, Rent: {self.rent}"

class Payment:
    def __init__(self, lease, amount, date):
        self.lease = lease
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"Payment for {self.lease.property.address}, Amount: {self.amount}, Date: {self.date}"

class MaintenanceRequest:
    def __init__(self, property, description, status="Pending"):
        self.property = property
        self.description = description
        self.status = status

    def __str__(self):
        return f"Request for {self.property.address}, {self.description}, Status: {self.status}"

# In-memory data storage for the example
properties = []
tenants = []
leases = []
payments = []
maintenance_requests = []

# Example usage
if __name__ == "__main__":
    # Creating example properties and tenants
    prop1 = Property("123 Elm St", 1200, "Apartment")
    prop2 = Property("456 Oak St", 1500, "House")
    prop3 = Property("789 Pine St", 1000, "Condo")
    properties.extend([prop1, prop2, prop3])

    tenant1 = Tenant("John Doe", "555-1234")
    tenant2 = Tenant("Jane Smith", "555-5678")
    tenant3 = Tenant("Jim Brown", "555-8765")
    tenants.extend([tenant1, tenant2, tenant3])

    # Creating leases
    lease1 = Lease(prop1, tenant1, "2023-01-01", "2024-01-01", 1200)
    lease2 = Lease(prop2, tenant2, "2023-02-01", "2024-02-01", 1500)
    lease3 = Lease(prop3, tenant3, "2023-03-01", "2024-03-01", 1000)
    leases.extend([lease1, lease2, lease3])

    # Creating payments
    payment1 = Payment(lease1, 1200, "2023-01-05")
    payment2 = Payment(lease2, 1500, "2023-02-05")
    payment3 = Payment(lease3, 1000, "2023-03-05")
    payments.extend([payment1, payment2, payment3])

    # Creating maintenance requests
    request1 = MaintenanceRequest(prop1, "Leaky faucet")
    request2 = MaintenanceRequest(prop2, "Broken window")
    request3 = MaintenanceRequest(prop3, "Faulty wiring")
    maintenance_requests.extend([request1, request2, request3])

    # Additional 20 Example Usage
    for i in range(4, 24):
        prop = Property(f"{i}0{i} Maple St", 1000 + i*50, "Apartment")
        tenant = Tenant(f"Tenant {i}", f"555-{i}000")
        lease = Lease(prop, tenant, "2023-01-01", "2024-01-01", 1000 + i*50)
        payment = Payment(lease, 1000 + i*50, f"2023-0{i}-05")
        request = MaintenanceRequest(prop, f"Issue {i}")

        properties.append(prop)
        tenants.append(tenant)
        leases.append(lease)
        payments.append(payment)
        maintenance_requests.append(request)

    # Function to retrieve tenant information by name
    def find_tenant(name):
        for tenant in tenants:
            if tenant.name == name:
                return tenant
        return None

    # Function to prompt for tenant's name and display their info
    def display_tenant_info():
        tenant_name = input("Enter tenant's name: ")
        tenant = find_tenant(tenant_name)
        if tenant:
            print(f"Tenant Info: {tenant}")
            related_lease = next((lease for lease in leases if lease.tenant == tenant), None)
            if related_lease:
                print(f"Lease Info: {related_lease}")
        else:
            print(f"Tenant {tenant_name} not found.")

    # Function to get type of maintenance request
    def request_maintenance():
        tenant_name = input("Enter tenant's name for maintenance request: ")
        tenant = find_tenant(tenant_name)
        if tenant:
            issue_description = input("Describe the maintenance issue: ")
            property_of_tenant = next((lease.property for lease in leases if lease.tenant == tenant), None)
            if property_of_tenant:
                request = MaintenanceRequest(property_of_tenant, issue_description)
                maintenance_requests.append(request)
                print(f"Request logged: {request}")
            else:
                print("No property found for this tenant.")
        else:
            print(f"Tenant {tenant_name} not found.")

    # Example: Display tenant info
    display_tenant_info()
    # Example: Log a maintenance request
    request_maintenance()
