import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kuapp.digitaluniversity.ac/SearchProvisionalResult.aspx"

results = []

# Exam Event value for May-2023 (Replace 'YOUR_EXAM_EVENT_VALUE_HERE' with the actual value)
exam_event_value = 'May-2023'

for roll_number in range(252001001, 252001076):
    payload = {
        'PRN Number Or Seat No/Roll no': str(roll_number),
        'Exam Event': exam_event_value
    }
    
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract data for each student and append it to the results list
        # Modify this part based on the structure of the HTML content
        # For example, you might need to find specific tags or classes containing the required information
        student_data = {}  # Create a dictionary to store student data
        
        # Extract and store data into the student_data dictionary
        # ...

        results.append(student_data)
    else:
        print(f"Failed to retrieve data for roll number {roll_number}")

# Convert the results list into a DataFrame using pandas
df = pd.DataFrame(results)

# Save the data to an Excel file
df.to_excel('student_results.xlsx', index=False)
