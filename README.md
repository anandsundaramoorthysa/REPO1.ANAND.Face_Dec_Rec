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
The Attendance System is a face recognition-based system developed during the Machine Learning Internship at Diffuse AI. The system is designed to automate the attendance process by using face recognition to log staff members' attendance. It captures attendance details such as date, name, and time ("In" and "Out"). The system records this information in CSV files named by the date, and the admin can view attendance records through the Admin page.

## Technologies Used
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For client-side validation and interactivity.
- **Bootstrap**: For responsive design and layout.
- **Python**: For server-side logic.
- **Flask**: Web framework for building the application.
- **OpenCV**: For face recognition processing.
- **Pandas**: For managing and processing attendance data.
- **CSV**: For storing attendance records.

## Page Overview and Functionality

### Home Page
**Purpose:** The Home Page provides an overview of the current day's attendance for staff members, allowing the "Time In" and "Time Out" to be recorded.

**Features:**
- **Navigation Bar**: Logo for "DiffuseAi" and navigation links to "Home" and "Admin" pages.
- **Attendance Overview**: Displays current day's attendance with buttons for recording "Time In" and "Time Out."
- **Attendance Table**: Shows a table with columns for staff name, roll number, time in, and time out.
- **Add New User**: Form to add new users by entering their name and user ID.

### Login Page
**Purpose:** Allows administrators to log into the system by providing their credentials.

**Features:**
- **Navigation Bar**: Includes links to "Home" and "Admin" pages.
- **Login Form**: Contains input fields for admin name and password, with client-side validation to ensure the credentials are correct.

### Admin Page
**Purpose:** Admins can view detailed attendance records, including time in/out data for each staff member.

**Features:**
- **Navigation Bar**: Links to "Home" and "Admin" pages.
- **Attendance Records Table**: Displays attendance data, indicating "Not Available" if data is missing.

## Installation
To set up the system locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anandsundaramoorthysa/REPO1.ANAND.Face_Dec_Rec.git
   cd attendance-system
   ```

2. **Install Dependencies**:
   Ensure Python is installed, then install the required packages:
   ```bash
   pip install face_recognition==1.3.0 dlib==19.22.1 cmake==3.20.0 Flask==2.3.2 OpenCV==4.7.0 NumPy==1.25.2 Pandas==2.0.3 scikit-learn==1.3.0 joblib==1.3.2 Werkzeug==2.3.4 Jinja2==3.1.2
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and go to `http://localhost:5000` to access the Attendance System.

## Usage
- **Mark Attendance**: On the Home Page, click "Time In" or "Time Out" to mark staff attendance.
- **Add New User**: Admins can add new staff through the "Add New User" form.
- **Admin Login**: Admins can log in via the Login Page to access detailed records.
- **View Attendance Records**: Admins can view detailed records on the Admin Page.

## Contributing
Contributions are welcome! Follow these steps:

1. **Fork the repository**:
   ```bash
   git fork https://github.com/anandsundaramoorthysa/REPO1.ANAND.Face_Dec_Rec.git
   ```

2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
   ```

3. **Make changes**: Implement your improvements or features.

4. **Submit a pull request**:
   ```bash
   git add .
   git commit -m "Describe your changes"
   git push origin feature-branch
   ```

5. **Submit a Pull Request**: Go to GitHub and create a pull request for review.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
If you have questions or want to collaborate, reach out:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Attendance%20using%20Face%20Recognition%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Attendance%20using%20Face%20Recognition%20Projects%20you%20developed%20during%20your%20Machine%20Learning%20Internship%20at%20Diffuse%20AI.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])
- **LinkedIn**: [Anand Sundaramoorthy](https://www.linkedin.com/in/anandsundaramoorthysa/)

## Results
1. **Home Page**:
   ![Home Page](https://github.com/anandsundaramoorthysa/REPO1.ANAND.Face_Dec_Rec/blob/main/1.Home%20Page.png)

2. **Login Page**:
   ![Login Page](https://github.com/anandsundaramoorthysa/REPO1.ANAND.Face_Dec_Rec/blob/main/2.Login%20Page%20for%20Admin%20page.png)

3. **Admin Page**:
   ![Admin Page](https://github.com/anandsundaramoorthysa/REPO1.ANAND.Face_Dec_Rec/blob/main/3.Admin%20Page.png)
