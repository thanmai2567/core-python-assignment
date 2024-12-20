def search_patients_by_disease(patients, disease):

    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]


def main():

    num_patients = int(input("Enter the number of patients: "))
    patients = []


    for _ in range(num_patients):
        name = input("Enter patient's name: ").strip()
        age = int(input("Enter patient's age: ").strip())
        disease = input("Enter patient's disease: ").strip()


        patient = {"Name": name, "Age": age, "Disease": disease}
        patients.append(patient)


    search_disease = input("\nEnter the disease to search for patients: ").strip()


    matching_patients = search_patients_by_disease(patients, search_disease)


    if matching_patients:
        print(f"Patients with {search_disease}: {matching_patients}")
    else:
        print(f"No patients found with the disease '{search_disease}'.")


if __name__ == "__main__":
    main()
