class patient:
    def __init__(self,Patient_id,name,age,disease):
        self.patient_id=Patient_id
        self.name=name
        self.age=age
        self.disease=disease

    def display(self):
        print("\nPatient Details")
        print("Patient_id:",self.patient_id)
        print("name:",self.name)
        print("age:",self.age)
        print("disease:",self.disease)
        print("-"*30)
        