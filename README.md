# Flexbody - Workout Planner Web Application

Flexbody is a responsive fitness web application built with Django and Python that empowers users to create, manage, and optimize personalized workout plans. Designed with a mobile-first approach and a scalable backend architecture, Flexbody provides a seamless experience for fitness enthusiasts to build their ideal routines.

## 🚀 Features

* **Secure User Authentication**: Robust registration and login system to protect user profiles and personal workout data.
* **Multimedia Exercise Library**: Browse a comprehensive database of exercises, complete with instructional images and video demonstrations.
* **Custom Workout Builder**: Create, edit, and organize custom workout routines through an intuitive user interface.
* **Admin Dashboard**: A centralized control panel for managing users, updating the exercise library, and overseeing application data.
* **Mobile-Friendly UI**: Fully responsive design ensuring a consistent and accessible experience across desktop, tablet, and mobile devices.

## 🛠️ Tech Stack

* **Backend**: Python, Django
* **Database**: SQLite (Development)
* **Frontend**: HTML5, CSS3, JavaScript 

## 🔮 Future Enhancements

* **Progress Tracking**: Log weights, sets, and reps to visualize strength and fitness progression over time.
* **Workout Scheduling**: Calendar integration to assign specific routines to different days of the week.

## ⚙️ Local Setup and Installation

### Prerequisites
* Python 3.8+
* pip and virtualenv

### Installation

1. **Clone the repository**
```bash
   git clone [https://github.com/klajdispahiu/Flexbody-.git](https://github.com/klajdispahiu/Flexbody-.git)
   cd flexbody
```

2. **Create and activate a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Apply database migrations**
```bash
   python manage.py migrate
```

5. **Create a superuser (for Admin Dashboard access)**
```bash
   python manage.py createsuperuser
```

6. **Run the development server**
```bash
   python manage.py runserver
```


7. **Access the application**
   * Main Web App: `(http://127.0.0.1:8000/)`
   * Admin Dashboard: `(http://127.0.0.1:8000/admin/)`


<img width="1360" height="725" alt="Screenshot 2026-05-23 at 6 51 29 PM" src="https://github.com/user-attachments/assets/d819b1ae-2147-4c6d-b638-c47f83409921" />
<img width="1368" height="736" alt="Screenshot 2026-05-23 at 6 54 44 PM" src="https://github.com/user-attachments/assets/2fcb2b8b-8628-4a12-a917-b3e87e984422" />
<img width="1372" height="776" alt="Screenshot 2026-05-23 at 6 55 07 PM" src="https://github.com/user-attachments/assets/38081be3-8301-4567-acf4-d8e6a9f1a657" />
<img width="1375" height="785" alt="Screenshot 2026-05-23 at 6 55 26 PM" src="https://github.com/user-attachments/assets/8a7b3996-31f4-457d-a8d0-0a0bfcd67069" />


