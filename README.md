<h1 align="center">Page Turners</h1>

Page Turners aims to provide an engaging and user-friendly platform for adult readers to discover and review books. The platform is designed for book enthusiasts who want to explore book details, save their favorite titles for future reading, and contribute to the community by leaving reviews. The target audience primarily consists of adult readers seeking to connect with like-minded individuals through book reviews. The site also provides functionality for admins to manage content efficiently, including the ability to moderate reviews and maintain the book database.

[Live project](https://book-club-acf9649c2594.herokuapp.com/)

[Django administration](https://book-club-acf9649c2594.herokuapp.com/admin/)

Admin Username: goca7

Password: Book_club

[Project Board](https://github.com/users/Goca7/projects/4)

## Contents (tba)

## User Experience (UX)

### User Stories

#### User Story: User Sign-Up 

- As a visitor, I want to sign up easily, so that I can join the Book Club.

- Acceptance Criteria:

  1. The sign-up form should have fields for username and password.

  2. Form validation must ensure that usernames are unique and in a valid format.

#### User Story: View Book Details 

- As a member, I want to view book details, so that I can learn more about specific titles before deciding to read them.

- Acceptance Criteria:

  1. Visitors should be able to click on a button to read more about the book.

  2. The book detail page must include user reviews.

  3. Non-members must have access to view book details without logging in.

#### User Story: Secure Login 

- As a member, I want to log in securely, so I can access my wish list and leave reviews.

- Acceptance Criteria:

  1. The login form must validate that the data entered by the user (username and password) is in the correct format before being submitted to the server.
 
  2. If the login credentials are correct, the user should be authenticated and redirected to their Want-to-read list.
 
  3. If the login credentials are incorrect, an error message should be displayed, prompting the user to try again.

#### User Story: Leave Review 

- As a member, I want to leave reviews for books I have read, so that I can share my opinions with other.

- Acceptance Criteria:

  1. Users must be logged in to submit a review.

  2. Reviews should be displayed with the user's name, submission date and review text.

  3. Users must have the option to edit or delete their reviews.

#### User Story: Add Books to "Want-to-read" List 

- As a member, I want to add books to my "Want-to-read" list, so that I can save books for future reading.

- Acceptance Criteria:

  1. Users should have an "Want-to-read" button on book listing page and each book detail page.

  2. The system must store the list under the user's profile and be accessible at any time.

  3. Users should have the ability to remove books from their "Want-to-read" list.

#### User Story: Receive Notifications 

- As a member, I want to receive notifications about my submissions, so that I know they were properly recorded.

- Acceptance Criteria:

  1. The system should send a notification when a user submits a book review.


#### User Story: Review Moderation 

- As an admin, I want to view and moderate members' reviews, so that I can ensure they are appropriate.
  
- Acceptance Criteria:

  1. Admins should be able to access a dashboard to see all user reviews.

  2. Admins must have the facility to delete inappropriate content.

#### User Story: Manage Database 

- As an admin, I want to add, edit, and delete books from the database, so that I can manage the content of the site.

- Acceptance Criteria:

  1. Admins should be able to create new book entries through a form.

  2. Admins must be able to edit book information like title, author, genre, and description.

  3. Admins must have the facility to delete books and their associated data.

#### User Story: Related Books 

- As a visitor, I want to see related books based on genre or author on the book detail page, so that I can discover similar titles that may interest me.

- Acceptance Criteria:

  1.  When a user views the book detail page, related books (based on genre or author) should be displayed at the bottom of the page.

  2.  Each related book should include the title, author, and a link to its detail page.

  3.  If there are no related books available, this section should be hidden or display a message like “No related books found.”


### Accessibility 

<img width="186" alt="WAVE_evaluation" src="https://github.com/user-attachments/assets/f38ba578-c679-4b23-a69a-69b314a0de2d">

<img width="244" alt="lighthouse_test" src="https://github.com/user-attachments/assets/33c27441-8233-41c4-a8e6-962be1a7521e">

- The Lighthouse and WAVE accessibility checks highlighted opportunities for improvements.

## Design

### Colour Scheme 

I chose colours that give the website a modern, minimalist look suitable for a reading-oriented platform.

- Background: Primarily white (#ffffff) for clean readability.
- Text Color: Dark shades like dark gray (#222222) for headings and regular text.
- Accent Color: Red (#ff0000) is used for call-to-action buttons (e.g., "Join Now") and hover effects.
- Navbar Links: Black or dark gray, transitioning to red on hover.
- Additional Backgrounds: Light gray (#f9f9f9) is used in specific sections like featured books for contrast.
  
![Colour Palette](https://github.com/user-attachments/assets/8d86ea5e-fa60-4c17-8d41-1c44c68592a4)

### Typography

The Lato font was used for body text and Roboto for headings. These are both clean and modern sans-serif fonts that work well for readability and a minimalist design.

These fonts are from google fonts and were imported into the style sheet.

### Imagery

Image by Pexels from Pixabay
Image by <a href="https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1853961">Pexels</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1853961">Pixabay</a>

The book cover images used on this website are sourced from Amazon.co.uk. This site is a student project created for educational purposes as part of coursework and is not intended for commercial use. All images belong to their respective copyright holders, and no infringement is intended. 

### Wireframes

#### Home Page

![Home_page_wireframes](https://github.com/user-attachments/assets/422deaee-e25b-4d60-90f8-3c2c3475e008)

#### Book Listing Page

![Book_listing_page_wireframes](https://github.com/user-attachments/assets/7477df84-8691-49ed-bf79-54b3164772e0)

#### Book Detail Page

![Book_detail_page_wireframes](https://github.com/user-attachments/assets/a0b7c7e8-278d-4f70-81cc-feefb7e19919)

####  Want-to-read-list Page

![User_profile_page_wireframes](https://github.com/user-attachments/assets/940159d9-e0f6-406c-9fff-280a57c9eccc)

### Existing Features 

#### Home Page

- Hero Section: A welcoming banner with a catchy tagline introducing the book club to potential users. Includes a "Join Now" call-to-action button, leading to the signup modal.

- Navigation Bar: A clean navigation bar allowing users to access the Home, Book Listings, and Login/Signup options. Responsive design ensures usability across devices.

- Featured Books: A carousel or grid showcasing a selection of popular or recently added books to engage visitors.

- About Section: A brief introduction to the purpose of the book club, its mission, and its target audience (adults).

- Login/Signup Modals: Pop-up forms for logging in or signing up, with proper form validation for secure user authentication.

- Footer: Contains links to privacy policy, contact information, and social media profiles.

#### Book Listing Page

- Book Grid: Display books in a clean, responsive grid format, with each book showing its title, author, rating, and a brief summary. Each book is clickable, leading to the detailed book page.

- Pagination: Ensure that the book listings are paginated, making it easy to navigate through large numbers of books without overwhelming the user.

- "Want-to-read" Button: Logged-in members can directly add a book to their "Want-to-read" list from the listing page.

#### Book Detail Page

- Book Information: Displays comprehensive details about the selected book, including the title, author, genre, publication date, synopsis, and rating.

- "Want-to-read" Button: Allows logged-in users to add the book to their "Want-to-read" list with a single click.

- Reviews Section: Shows reviews from other members, including the reviewer's name, rating, and comment. Logged-in users can leave their own review.

- Navigation Links: Quick links back to the book listings page or Home page

#### Want-to-read-list Page

- "Want-to-read" list: This is the primary place where users can view and manage their saved books. This
  page will display all the books that the user has previously added. 

- Each entry in the list will have buttons to either remove the book from the list or navigate to the book detail page for more information.

- Users will receive a confirmation message confirming the successful book deletion.

### Future Features

### Book Detail Page

- Related Books: At the bottom of the page, suggest similar or related books based on the genre or author.

### User Flow Diagrams

<img width="238" alt="book_club_visitor_flowchart_reduced" src="https://github.com/user-attachments/assets/746d33c6-d1bf-4012-ab56-639b6437a6f6">

<img width="408" alt="book_club_member_flowchart_reduced" src="https://github.com/user-attachments/assets/6b1fa831-8b5e-42a5-a173-417e2b8b7b31">

<img width="581" alt="book_club_admin_flowchart_reduced" src="https://github.com/user-attachments/assets/8df23cf0-f69b-4792-b156-69d8bb25c18b">

## Data Models

### Book Model:

- Each book in our club will have attributes such as title, author, description, and published date.

### Review Model:

- The Review model will store reviews users leave for each book. It is linked both to the Book and the User models.

### User Model:

- The User model is provided by Django.

### Relationships:

#### User <-> Review:

- One-to-many relationship: One user can write multiple reviews, but each review belongs to only one user.

- Foreign Key: user_id in the Review table references the id in the User table.

#### Book <-> Review:

- One-to-many relationship: One book can have multiple reviews, but each review is linked to only one book.

- Foreign Key: book_id in the Review table references the id in the Book table.

![book_club_tables_in_database1](https://github.com/user-attachments/assets/5a7e87a1-a211-40be-adb0-a4ec6bc57e07)

![book_club_tables_in_database2](https://github.com/user-attachments/assets/376a960a-3afd-49fd-87c4-b254507e65d3)

### ER Diagram

![book_club_ER_diagram](https://github.com/user-attachments/assets/ede5057d-209f-4436-b888-4c46f9eabb73)

## Technologies Used 

- HTML5
- CSS3
- Javascript
- Python3
- Django4
- Bootstrap5
- Markdown Builder
- Git
- GitHub
- PostgreSQL
- Heroku
- WhiteNoise
- Gunicorn
- Psycopg2
- Allauth
- Favicon Generator
- Logo Generator
- Coolors
- Google Fonts
- Visily
- Lucidchart
- Figma
- MS Word
- TinyPNG
- ChatGPT (used for debugging and troubleshooting)
- W3C HTML Markup Validator
- W3C Jigsaw CSS Validator
- JS Hint
- Lighthouse
- WAVE
- CI Python Linter

## Agile Methodology (tba)

## Deployment and Local Development (tba)

## Testing

### Validation of HTML, CSS, JS, and Python Code
Validation tools used are [Nu HTML Checker](https://validator.w3.org/nu/), [Jigsaw](https://jigsaw.w3.org/css-validator/), [JSHint](https://jshint.com/), [PEP8 codeInst](https://pep8ci.herokuapp.com) and [Python Syntax Checker](https://extendsclass.com/python-tester.html).

#### HTML Validation

<img width="680" alt="html_validation_index" src="https://github.com/user-attachments/assets/b7d1eb07-9cf8-4273-a070-f8d105751fbe">
<img width="685" alt="html_validation_booklisting" src="https://github.com/user-attachments/assets/64f33cec-542d-45fb-a81a-f27e76a7fde9">


<img width="678" alt="html_validation_booklisting_page2" src="https://github.com/user-attachments/assets/8890f75e-c501-4b65-a8ad-0cca69ab6b44">
<img width="677" alt="html_validation_theslave" src="https://github.com/user-attachments/assets/ec168b32-8c26-43d6-a220-77b46b77c2e3">
<img width="678" alt="html_validation_brightonrock" src="https://github.com/user-attachments/assets/50d0634e-5737-445d-b1f3-a893bedfb255">
<img width="679" alt="html_validation_demian" src="https://github.com/user-attachments/assets/bf6a5fff-d712-4fda-bc5d-47b9dfbd45ac"><img width="665" alt="html_validation_thebridge" src="https://github.com/user-attachments/assets/d242a3ae-700c-460a-a708-da484a4cc013">

#### CSS Validation

<img width="763" alt="css_validation" src="https://github.com/user-attachments/assets/307792fa-0fea-4c61-9071-d7ca33baebdb">

#### Javascript Validation

<img width="548" alt="js_validation" src="https://github.com/user-attachments/assets/ac1948ad-0563-4df1-b3d9-8b2d7cc40f44">

#### Python Validation

<img width="736" alt="python_syntax_books_views" src="https://github.com/user-attachments/assets/16ee12cf-ad55-4a5f-8d3f-4dac95cd17ff">
<img width="736" alt="python_syntax_reviews_views" src="https://github.com/user-attachments/assets/95e427da-f268-4b93-9087-b393dc12bf00">
<img width="745" alt="python_syntax_wish_list_views" src="https://github.com/user-attachments/assets/f1558a69-c34f-4909-9dc0-654d09739058">
<img width="578" alt="python_linter_books_views" src="https://github.com/user-attachments/assets/78dc8ad5-8fb8-49ec-9afa-f9eebc903406">
<img width="566" alt="python_linter_reviews_views" src="https://github.com/user-attachments/assets/1c6db330-4db9-4bd9-b34c-9262f224d2d4">
<img width="557" alt="python_linter_wishlist_views" src="https://github.com/user-attachments/assets/29a1732d-498d-41d6-a174-88e5c2a4403e">

### Manual Testing 

![Manual_Testing_Results-1](https://github.com/user-attachments/assets/3cee3ace-f611-4051-bb45-2214aaa13cb7)

![Manual_Testing_Results-2](https://github.com/user-attachments/assets/724c2aff-b00b-401b-8b05-1c2f45197fb7)

### Responsive Design

<img width="627" alt="responsivness_test" src="https://github.com/user-attachments/assets/6eaee6fb-df74-440f-b6de-edadddae818a">

## SECRET_KEY

- I created a new SECRET_KEY and set it as an environment variable in the env.py file. I modified the settings.py file to retrieve the new SECRET_KEY from the environment variables. To ensure the security of my Django app on Heroku, I set the SECRET_KEY as a config variable on Heroku as well.

## Credits 

- Hero image by Pexels from Pixabay
- Book cover images by Amazon UK
- Animation by Video Effects on YouTube
- Content by Claude 3 

