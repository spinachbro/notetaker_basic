# Basic Notetaker

A modern, responsive Flask web application for organizing and tracking your learning notes. Built with a beautiful blue-themed design and intuitive user interface.

## Features

- **User Authentication**: Secure registration and login system
- **Topic Organization**: Create and manage topics to categorize your notes
- **Entry Management**: Add detailed entries to each topic with timestamps
- **Modern UI**: Responsive design with blue accent colors
- **Edit Functionality**: Update your entries anytime
- **Mobile Friendly**: Works perfectly on all devices

## Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## Usage

### Getting Started
1. Register a new account or login with existing credentials
2. Create your first topic (e.g., "Python Programming", "Cooking Recipes")
3. Add entries to your topics to track your learning
4. Edit entries anytime to update your notes

### Features Overview
- **Home Page**: Welcome screen with app overview and quick actions
- **Topics**: View all your topics with entry counts
- **Add Topic**: Create new topics to organize your notes
- **View Topic**: See all entries for a specific topic
- **Add Entry**: Write detailed notes for any topic
- **Edit Entry**: Update your notes anytime

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: Bootstrap 5 with custom CSS
- **Icons**: Font Awesome
- **Styling**: Custom blue theme with modern gradients

## File Structure

```
notetaker-basic/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── index.html        # Home page
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   ├── topics.html       # Topics list
│   ├── new_topic.html    # New topic form
│   ├── topic.html        # Topic detail view
│   ├── new_entry.html    # New entry form
│   └── edit_entry.html   # Edit entry form
└── notetaker.db         # SQLite database (created automatically)
```

## Customization

The app uses a blue color scheme that can be easily customized by modifying the CSS variables in `templates/base.html`:

```css
:root {
    --primary-blue: #007bff;
    --secondary-blue: #17a2b8;
    --dark-blue: #0056b3;
    --light-blue: #d1ecf1;
    --accent-blue: #004085;
}
```

## Security Features

- Password hashing using Werkzeug
- User session management with Flask-Login
- CSRF protection (built into Flask)
- User-specific data isolation

## Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## License

This project is open source and available under the MIT License. 