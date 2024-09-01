# Face Recognition Attendance System

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Page Overview and Functionality](#page-overview-and-functionality)
  - [Home Page](#home-page)
  - [Login Page](#login-page)
  - [Admin Page](#admin-page)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Results](#results)

## Introduction
The Attendance System is a face recognition-based system developed during the Machine Learning Internship at Diffuse AI. The system is designed to automate the attendance process by using face recognition to log staff members' attendance. It capturing attendance details such as date, name, and time (both "In" and "Out"). The system records this information in CSV files named by the date, and the admin can view attendance records through the Admin page.

## Technologies Used
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For client-side validation and interactivity.
- **Bootstrap**: For responsive design and layout.
- **Python**: For server-side logic.
- **Flask**: As the web framework for building the application.
- **OpenCV**: For face recognition processing.
- **Pandas**: For managing and processing attendance data.
- **CSV**: For storing attendance records.

## Page Overview and Functionality

### Home Page
**Purpose:** The Home Page of the attendance system provides an overview of the current day's attendance for staff members. It includes functionality for marking the "Time In" and "Time Out" for staff members, displaying the recorded attendance in a tabular format.

**Features:**
- **Navigation Bar:** Includes a logo for "DiffuseAi" and navigation links to "Home" and "Admin" pages.
- **Attendance Overview:** Displays a summary of the current day's attendance with buttons for recording "Time In" and "Time Out."
- **Attendance Table:** Shows a table with columns for staff name, roll number, time in, and time out.
- **Add New User:** Includes a form to add new users to the system by entering their name and user ID.

### Login Page
**Purpose:** The Login Page allows administrators to log into the system by providing their credentials. It is a simple form-based login page that verifies the admin name and password.

**Features:**
- **Navigation Bar:** Similar to the Home Page, with navigation links to "Home" and "Admin" pages.
- **Login Form:** Contains input fields for admin name and password. The form uses client-side JavaScript validation to check if the credentials match the predefined values. If the credentials are correct, the user is redirected to the Admin page; otherwise, an error message is displayed.

### Admin Page
**Purpose:** The Admin Page is designed to allow administrators to view detailed attendance records. It presents the attendance data in a table format, showing the name, roll number, time in, time out, and the date for each record.

**Features:**
- **Navigation Bar:** As in the previous pages, with links to "Home" and "Admin."
- **Attendance Records Table:** Displays detailed records of attendance, including information on whether the time in or time out was not available (represented as "Not Available" if missing).

## Installation
To set up the Attendance System on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec.git
   cd attendance-system
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then install the required packages using pip:
   ```bash
   pip install face_recognition==1.3.0 dlib==19.22.1 cmake==3.20.0 Flask==2.3.2 OpenCV==4.7.0 NumPy==1.25.2 Pandas==2.0.3 scikit-learn==1.3.0 joblib==1.3.2 Werkzeug==2.3.4 Jinja2==3.1.2
   ```

3. **Run the Application**:
   Start the Flask server by running:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` to access the Attendance System.

## Guidelines
If you encounter errors or issues running the project in VS Code, consider using a virtual environment:

**Note:** Before doing so, place the project folder inside another folder, and create a virtual environment within that folder.

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     
## Usage
- **Mark Attendance**: On the Home Page, staff members can mark their attendance by clicking the "Time In" or "Time Out" buttons.
- **Add New User**: Admin can add new staff members to the system using the "Add New User" form.
- **Admin Login**: Admin can log in through the Login Page to access detailed attendance records.
- **View Attendance Records**: Once logged in, the admin can view detailed attendance records on the Admin Page.

## Contributing
Contributions are welcome! Please follow these steps:

1. **Fork the repository**:
   ```bash
   git fork https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec.git
   ```

2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```

3. **Make your changes**: Implement your improvements or new features.

4. **Submit a pull request**:
   ```bash
   git add .
   git commit -m "Describe your changes"
   git push origin feature-branch
   ```
   Then, go to the repository on GitHub and create a Pull Request.

6. **Submit a Pull Request**:
   Go to the original repository on GitHub and click on "Pull Request" to submit your changes for review.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or would like to collaborate, feel free to reach out:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Attendance%20using%20Face%20Recognition%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Attendance%20using%20Face%20Recognition%20Projects%20you%20developed%20during%20your%20Machine%20Learning%20Internship%20at%20Diffuse%20AI.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])
- **LinkedIn**: [Anand's LinkedIn Profile](https://www.linkedin.com/in/anands37/)

## Results
1. **Home Page**:
   ![Home Page](https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec/blob/main/1.Home%20Page.png)

2. **Login Page**:
   ![Login Page](https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec/blob/main/2.Login%20Page%20for%20Admin%20page.png)

3. **Admin Page**:
   ![Admin Page](https://github.com/a1n13a1n13d4/REPO1.ANAND.Face_Dec_Rec/blob/main/3.Admin%20Page.png)

