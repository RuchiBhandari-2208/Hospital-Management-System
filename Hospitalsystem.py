from Hospital import patient

class hospitalsystem:

    def __init__(self):
        self.patients=[]

    def Add_patient(self):
        Patient_id=int(input("Enter patient id:"))
        name=input("Enter patient name:")
        age=int(input("Enter patient Age:"))
        disease=input("Enter disease:")

        New_patient=patient(Patient_id,name,age,disease)
        self.patients.append(New_patient)

        print("patient added successfully.")

    def display_patient(self):
        print(self.patients)   #test
        
        if len(self.patients)==0:
            print("No patient record found.")
        else:
            for patient in self.patients:
                patient.display()

    def search_patient(self):
        patient_id = int(input("Enter Patient ID to search: "))
 
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.display()
                return
            
            print("Patient not found.")

    def update_patient(self):
        patient_id = int(input("Enter Patient ID: "))
 
        for patient in self.patients:
            if patient.patient_id == patient_id:
                new_disease = input("Enter New Disease: ")
                patient.disease = new_disease
                print("Disease updated successfully!")
                return
 
        print("Patient not found.")

        
       
    def delete_patient(self):
        patient_id = int(input("Enter Patient ID to delete: "))
 
        for patient in self.patients:
            if patient.patient_id == patient_id:
                self.patients.remove(patient)
                print("Patient record deleted successfully!")
                return
 
        print("Patient not found.")
 

    