import cv2
import os
from flask import Flask, request, render_template, redirect, session, url_for
from datetime import date
from datetime import datetime
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import joblib

# Defining Flask App
app = Flask(__name__)

nimgs = 10

# Saving Date today in 2 different formats
datetoday = date.today().strftime("%m_%d_%y")
datetoday2 = date.today().strftime("%d-%B-%Y")

# Initializing VideoCapture object to access WebCam
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# If these directories don't exist, create them
if not os.path.isdir('Attendance'):
    os.makedirs('Attendance')
if not os.path.isdir('static'):
    os.makedirs('static')
if not os.path.isdir('static/faces'):
    os.makedirs('static/faces')
if f'Attendance-{datetoday}.csv' not in os.listdir('Attendance'):
    with open(f'Attendance/Attendance-{datetoday}.csv', 'w') as f:
        f.write('Name,Roll,Time In,Time Out\n')

# get a number of total registered users
def totalreg():
    return len(os.listdir('static/faces'))

# extract the face from an image
def extract_faces(img):
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_points = face_detector.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
        return face_points
    except cv2.error as e:
        print(f"OpenCV error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []


# Identify face using ML model
def identify_face(facearray):
    model_path = 'static/face_recognition_model.pkl'
    if not os.path.exists(model_path):
        raise FileNotFoundError("Face recognition model not found.")
    model = joblib.load(model_path)
    return model.predict(facearray)

# A function which trains the model on all the faces available in faces folder
def train_model():
    faces = []
    labels = []
    userlist = os.listdir('static/faces')
    for user in userlist:
        for imgname in os.listdir(f'static/faces/{user}'):
            img = cv2.imread(f'static/faces/{user}/{imgname}')
            resized_face = cv2.resize(img, (50, 50))
            faces.append(resized_face.ravel())
            labels.append(user)
    faces = np.array(faces)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces, labels)
    joblib.dump(knn, 'static/face_recognition_model.pkl')

# Extract info from today's attendance file in attendance folder
def extract_attendance():
    df = pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')
    
    # Ensure all expected columns exist
    required_columns = ['Name', 'Roll', 'Time In', 'Time Out']
    for col in required_columns:
        if col not in df.columns:
            df[col] = ''  # Add missing columns with empty values
    
    names = df['Name']
    rolls = df['Roll']
    times_in = df['Time In']
    times_out = df['Time Out']
    l = len(df)
    return names, rolls, times_in, times_out, l

def update_attendance(name, time_type):
    username = name.split('_')[0]
    userid = name.split('_')[1]
    current_time = datetime.now().strftime("%H:%M:%S")
    file_path = f'Attendance/Attendance-{datetoday}.csv'

    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            f.write('Name,Roll,Time In,Time Out\n')

    df = pd.read_csv(file_path)

    if int(userid) in df['Roll'].values:
        if time_type == 'Time In':
            df.loc[df['Roll'] == int(userid), 'Time In'] = current_time
        elif time_type == 'Time Out':
            df.loc[df['Roll'] == int(userid), 'Time Out'] = current_time
        else:
            raise ValueError("Invalid time_type. Must be 'Time In' or 'Time Out'.")
        df.to_csv(file_path, index=False, mode='w', header=True)
    else:
        if time_type == 'Time In':
            with open(file_path, 'a', newline='') as f:
                f.write(f'{username},{userid},{current_time},\n')
        elif time_type == 'Time Out':
            with open(file_path, 'a', newline='') as f:
                f.write(f'{username},{userid},,{current_time}\n')

## A function to get names and roll numbers of all users
def getallusers():
    userlist = os.listdir('static/faces')
    names = []
    rolls = []
    l = len(userlist)

    for i in userlist:
        name, roll = i.split('_')
        names.append(name)
        rolls.append(roll)

    return userlist, names, rolls, l

## A function to delete a user folder 
def deletefolder(duser):
    pics = os.listdir(duser)
    for i in pics:
        os.remove(duser+'/'+i)
    os.rmdir(duser)

################## ROUTING FUNCTIONS #########################

# Our main page
@app.route('/')
def index():
    names, rolls, times_in, times_out, l = extract_attendance()  # Extract updated data
    zipped_data = zip(names, rolls, times_in, times_out)
    return render_template('index.html', zipped_data=zipped_data, totalreg=totalreg(), datetoday2=datetoday2)

# Handle Time In request
@app.route('/time_in', methods=['GET'])
def time_in():
    if 'face_recognition_model.pkl' not in os.listdir('static'):
        names, rolls, times_in, times_out, l = extract_attendance()
        return render_template('index.html', names=names, rolls=rolls, times_in=times_in, times_out=times_out, l=l, totalreg=totalreg(), datetoday2=datetoday2, mess='There is no trained model in the static folder. Please add a new face to continue.')

    ret = True
    cap = cv2.VideoCapture(0)
    while ret:
        ret, frame = cap.read()
        faces = extract_faces(frame)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (86, 32, 251), 1)
                cv2.rectangle(frame, (x, y), (x+w, y-40), (86, 32, 251), -1)
                face = cv2.resize(frame[y:y+h, x:x+w], (50, 50))
                identified_person = identify_face(face.reshape(1, -1))[0]
                
                # Check if already recorded
                names, rolls, times_in, times_out, l = extract_attendance()
                userid = identified_person.split('_')[1]
                if int(userid) in pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')['Roll'].values:
                    if pd.read_csv(f'Attendance/Attendance-{datetoday}.csv').loc[pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')['Roll'] == int(userid), 'Time In'].values[0]:
                        mess = 'You have already checked in today.'
                    else:
                        update_attendance(identified_person, 'Time In')
                        mess = 'Time In recorded successfully.'
                else:
                    update_attendance(identified_person, 'Time In')
                    mess = 'Time In recorded successfully.'
                
                cv2.putText(frame, f'{identified_person}', (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow('Time In', frame)
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    # Refresh data
    names, rolls, times_in, times_out, l = extract_attendance()
    return render_template('index.html', names=names, rolls=rolls, times_in=times_in, times_out=times_out, l=l, totalreg=totalreg(), datetoday2=datetoday2, mess=mess)


    # Refresh data
    names, rolls, times_in, times_out, l = extract_attendance()
    return render_template('index.html', names=names, rolls=rolls, times_in=times_in, times_out=times_out, l=l, totalreg=totalreg(), datetoday2=datetoday2)

# Handle Time Out request
@app.route('/time_out', methods=['GET'])
def time_out():
    if 'face_recognition_model.pkl' not in os.listdir('static'):
        names, rolls, times_in, times_out, l = extract_attendance()
        return render_template('index.html', names=names, rolls=rolls, times_in=times_in, times_out=times_out, l=l, totalreg=totalreg(), datetoday2=datetoday2, mess='There is no trained model in the static folder. Please add a new face to continue.')

    ret = True
    cap = cv2.VideoCapture(0)
    while ret:
        ret, frame = cap.read()
        faces = extract_faces(frame)
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (86, 32, 251), 1)
                cv2.rectangle(frame, (x, y), (x+w, y-40), (86, 32, 251), -1)
                face = cv2.resize(frame[y:y+h, x:x+w], (50, 50))
                identified_person = identify_face(face.reshape(1, -1))[0]
                
                # Check if already recorded
                names, rolls, times_in, times_out, l = extract_attendance()
                userid = identified_person.split('_')[1]
                if int(userid) in pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')['Roll'].values:
                    if pd.read_csv(f'Attendance/Attendance-{datetoday}.csv').loc[pd.read_csv(f'Attendance/Attendance-{datetoday}.csv')['Roll'] == int(userid), 'Time Out'].values[0]:
                        mess = 'You have already checked out today.'
                    else:
                        update_attendance(identified_person, 'Time Out')
                        mess = 'Time Out recorded successfully.'
                else:
                    update_attendance(identified_person, 'Time Out')
                    mess = 'Time Out recorded successfully.'
                
                cv2.putText(frame, f'{identified_person}', (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.imshow('Time Out', frame)
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    # Refresh data
    names, rolls, times_in, times_out, l = extract_attendance()
    return render_template('index.html', names=names, rolls=rolls, times_in=times_in, times_out=times_out, l=l, totalreg=totalreg(), datetoday2=datetoday2, mess=mess)

# A function to add a new user.
@app.route('/add', methods=['POST'])
def add():
    newusername = request.form.get('newusername', '').strip()
    newuserid = request.form.get('newuserid', '').strip()

    if not newusername or not newuserid:
        return render_template('index.html', totalreg=totalreg(), datetoday2=datetoday2, mess='Username and UserID are required.')

    new_folder = f'static/faces/{newusername}_{newuserid}'
    if not os.path.isdir(new_folder):
        os.makedirs(new_folder)
        return render_template('index.html', totalreg=totalreg(), datetoday2=datetoday2)
    else:
        return render_template('index.html', totalreg=totalreg(), datetoday2=datetoday2, mess='User already exists.')

# Deleting a user folder
@app.route('/delete', methods=['POST'])
def delete():
    deleteuser = request.form['deleteuser']
    deletefolder(deleteuser)
    return render_template('index.html', totalreg=totalreg(), datetoday2=datetoday2)

@app.route('/login')
def login():
    return render_template('login.html')

# Extract Attendance
def extract_attendance():
    try:
        df = pd.read_csv(f'Attendance/Attendance-{datetoday}.csv', on_bad_lines='skip')
    except pd.errors.ParserError as e:
        print(f"ParserError: {e}")
        return [], [], [], [], 0

    required_columns = ['Name', 'Roll', 'Time In', 'Time Out']
    for col in required_columns:
        if col not in df.columns:
            df[col] = ''  

    names = df['Name'].tolist()
    rolls = df['Roll'].tolist()
    times_in = df['Time In'].tolist()
    times_out = df['Time Out'].tolist()
    l = len(df)
    return names, rolls, times_in, times_out, l

# Shown Attendance data in Admin Page
def get_all_attendance():
    attendance_files = os.listdir('Attendance')
    all_attendance = []
    for file in attendance_files:
        if file.endswith('.csv'):
            date_str = file.split('-')[1].split('.')[0]
            date_formatted = datetime.strptime(date_str, "%m_%d_%y").strftime("%d-%B-%Y")
            try:
                df = pd.read_csv(f'Attendance/{file}', on_bad_lines='skip')
            except pd.errors.ParserError as e:
                print(f"ParserError: {e}")
                continue
            df['Date'] = date_formatted
            all_attendance.append(df)
    
    if all_attendance:
        combined_df = pd.concat(all_attendance).reset_index(drop=True)
    else:
        combined_df = pd.DataFrame(columns=['Name', 'Roll', 'Time In', 'Time Out', 'Date'])

    combined_df = combined_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return combined_df

#Our admin paged
@app.route('/admin')
def admin():
    all_attendance = get_all_attendance()
    records = all_attendance.to_dict(orient='records')
    return render_template('admin.html', tables=records)

# Main Entry Point
if __name__ == '__main__':
    app.run(debug=True)
