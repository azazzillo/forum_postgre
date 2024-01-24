# Forum with Quotes
Welcome to the Forum with Quotes project, a Flask-powered forum where users can share, comment, and rate quotes. The project utilizes PostgreSQL as its database and provides features such as posting quotes, commenting, rating, and user registration/authentication.

## Features:
* **User Authentication:**Users can register and log in securely, providing a personalized experience for posting quotes, commenting, and engaging with the community.
* **Quote Posting:** Share your favorite quotes with the community by creating new posts. Each quote post includes details like the author, source, and the actual quote itself.
* **Commenting System:** Engage in discussions by commenting on quote posts. Share thoughts, insights, and reactions with other community members.
* **Rating System:** Users can rate quotes based on their preferences, allowing the community to highlight the most popular and appreciated quotes.
* **Post Management:** Edit and delete your own quotes and comments to maintain control over your contributions to the forum.
* **Post Sorting:** Explore quotes based on different sorting options, such as popularity, date, or user ratings, enhancing the user experience.

## Getting Started:
1. Clone the Repository:
   ```
   git clone https://github.com/your-username/your-forum-with-quotes.git
   ```
2. Install Dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set Up PostgreSQL Database:
   * Create a PostgreSQL database and update the database configuration in the project accordingly.
     
4. Run Migrations:
   ```
   python manage.py db upgrade
   ```
5. Start the Development Server:
   ```
   python app.py
   ```
6. Visit the Forum:
   Open your web browser and navigate to http://localhost:5000 to explore the Forum with Quotes.



