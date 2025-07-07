# YouTube Clone (React + Django)

This is a full-stack YouTube-like application built using Django for the backend and React for the frontend. Users can register, log in, upload videos, watch videos, like them, and add them to a watch later list.

## Features

- User registration and login
- Token-based authentication
- Upload videos with title and description
- View all uploaded videos
- Play videos in-browser
- Like videos (stored in session)
- Watch later functionality (stored in session)
- Share video links
- Navigation through a responsive navbar

## Technology Stack

### Frontend
- React
- React Router
- Axios
- Tailwind CSS or plain CSS

### Backend
- Django
- Django REST Framework
- Token Authentication
- SQLite (default DB)

## Project Structure

```
youtube_clone_final/
├── backend_main/           # Django backend
│   ├── api/                # Django app
│   ├── backend/            # Project settings
│   ├── media/              # Uploaded videos
│   └── manage.py
│
├── mini-youtube-clone/     # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
└── requirements.txt
```

## Getting Started

### Backend (Django)

```bash
cd backend_main
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend (React)

```bash
cd mini-youtube-clone
npm install
npm run dev
```

Then visit: `http://localhost:5173`

---

## Notes

- Make sure both frontend and backend servers are running.
- Videos are stored locally in the `media/videos/` directory.

