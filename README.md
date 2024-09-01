# Face Recognition Attendance System
---
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

## Introduction
The Attendance System is a face recognition-based system developed during the Machine Learning Internship at Diffuse AI. The system is designed to automate the attendance process by using face recognition to log staff members' attendance. It operates daily from 8 AM to 6 PM, capturing attendance details such as date, name, and time (both "In" and "Out"). The system records this information in CSV files named by the date, and the admin can view attendance records through the Admin page.

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
   git clone https://github.com/yourusername/attendance-system.git
   cd attendance-system
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask server by running:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your web browser and go to `http://localhost:5000` to access the Attendance System.

## Usage
- **Mark Attendance**: On the Home Page, staff members can mark their attendance by clicking the "Time In" or "Time Out" buttons.
- **Add New User**: Admin can add new staff members to the system using the "Add New User" form.
- **Admin Login**: Admin can log in through the Login Page to access detailed attendance records.
- **View Attendance Records**: Once logged in, the admin can view detailed attendance records on the Admin Page.

## Contributing
We welcome contributions to improve this project. If you would like to contribute, please follow these steps:

1. **Fork the Repository**: 
   Click on the "Fork" button at the top right corner of this page to create a copy of the repository in your GitHub account.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/attendance-system.git
   cd attendance-system
   ```

3. **Create a Branch**:
   Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-or-bugfix-name
   ```

4. **Make Your Changes**:
   Implement your feature or fix.

5. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Description of the feature or fix"
   git push origin feature-or-bugfix-name
   ```

6. **Submit a Pull Request**:
   Go to the original repository on GitHub and click on "Pull Request" to submit your changes for review.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For inquiries or further information about the project, you can reach me via LinkedIn at [Anand S](https://www.linkedin.com/in/anands37/) or email at sanand03072005@gmail.com with the subject "Inquiry About Attendance using Face Recognition Project."
