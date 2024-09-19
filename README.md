<h1 align="center">Page Turners</h1>

Page Turners aims to provide an engaging and user-friendly platform for adult readers to discover and review books. The platform is designed for book enthusiasts who want to explore book details, save their favorite titles for future reading, and contribute to the community by leaving reviews. The target audience primarily consists of adult readers seeking to connect with like-minded individuals through book reviews. The site also provides functionality for admins to manage content efficiently, including the ability to moderate reviews and maintain the book database. 

[Live project] (https://

## Table of Contents (tba)

## User Stories

#### User Story: User Sign-Up (Must Have)
- As a visitor, I want to sign up easily, so that I can join the Book Club.

- Acceptance Criteria:

  1. The sign-up form should have fields for username and password.

  2. Form validation must ensure that usernames are unique and in a valid format.

#### User Story: View Book Details (Must Have)
- As a visitor, I want to sign up easily, so that I can join the Book Club.

- Acceptance Criteria:

  1. Visitors should be able to click on a book title to view its details (title, author, genre, description).

  2. The book detail page must include user reviews and ratings.

  3. Non-members must have access to view book details without logging in.

#### User Story: Secure Login (Must Have)
- As a member, I want to view book details, so that I can learn more about specific titles before deciding to read them.

- Acceptance Criteria:

  1. The data entered by the user into the login form (username and password) is correct and in the proper format before it is submitted to the server for processing.
  
#### User Story: Leave Review (Must Have)  
- As a member, I want to leave reviews for books I have read, so that I can share my opinions with other.

- Acceptance Criteria:

    1. Users must be logged in to submit a review.

    2. Reviews should be displayed with the user's name, rating (1–5 stars), and review text.

    3. Users must have the option to edit or delete their reviews.

#### User Story: Add Books to "Want-to-read" List (Must Have)
- As a member, I want to add books to my "Want-to-read" list, so that I can save books for future reading.

- Acceptance Criteria:

  1. Users should have an "Want-to-read" button on each book detail page.

  2. The system must store the list under the user's profile and be accessible at any time.

  3. Users should have the ability to remove books from their "Want-to-read" list.

#### User Story: Receive Notifications (Must Have)
- As a member, I want to receive notifications about my submissions, so that I know they were properly recorded.

- Acceptance Criteria:

  1. The system should send a notification when a user submits a book review.
 
#### User Story: Account Deletion (Must Have)
- As a member, I want to delete my account easily, so that I can remove my personal data and stop using the platform.

- Acceptance Criteria:

  1. The user can navigate to the profile page and find a "Delete Account" button.

  2. Upon clicking the button, a confirmation prompt appears, asking the user to confirm the deletion.

  3. The system permanently deletes the user’s account and associated data (e.g., reviews, "Want-to-read" list) upon confirmation.

  4. The user receives a confirmation message notifying them that their account has been deleted.

  5. After deletion, the user can no longer log in with the deleted account credentials.

#### User Story: Review Moderation (Must Have)
- As an admin, I want to view and moderate members' reviews, so that I can ensure they are appropriate.
  
- Acceptance Criteria:

  1. Admins should be able to access a dashboard to see all user reviews and comments.

  2. Admins must have the ability to delete inappropriate content.

#### User Story: Manage Database (Must Have)
- As an admin, I want to add, edit, and delete books from the database, so that I can manage the content of the site.

- Acceptance Criteria:

  1. Admins should be able to create new book entries through a form.

  2. Admins must be able to edit book information like title, author, genre, and description.

  3. Admins must have the ability to delete books and their associated data.
 
#### User Story: Related Books (Could Have)

 - As a visitor, I want to see related books based on genre or author on the book detail page, so that I can discover similar titles that may interest me.

 - Acceptance Criteria:

   1. When a user views the book detail page, related books (based on genre or author) should be displayed at the bottom of the page.

   2. The system should display at least three related books in a horizontal scroll or grid format.

   3. Each related book should include the title, author, and a link to its detail page.
   
   4. If there are no related books available, this section should be hidden or display a message like “No related books found.”

   5. The related books must be relevant, showing books from the same genre or by the same author as the currently viewed book. 
 
## Existing Features (MVP)

### Home Page

  - Hero Section: A welcoming banner with a catchy tagline introducing the book club to potential users. Includes a "Join Now" call-to-action button, leading to the signup modal.
 
  - Navigation Bar: A clean navigation bar allowing users to access the Home, Book Listings, and Login/Signup options. Responsive design ensures usability across devices.
 
  - Featured Books: A carousel or grid showcasing a selection of popular or recently added books to engage visitors.
 
  - About Section: A brief introduction to the purpose of the book club, its mission, and its target audience (adults).
 
  - Login/Signup Modals: Pop-up forms for logging in or signing up, with proper form validation for secure user authentication.
 
  - Footer: Contains links to privacy policy, contact information, and social media profiles.
 
### Book Listing Page

  - Book Grid: Display books in a clean, responsive grid format, with each book showing its title, author, rating, and a brief summary. Each book is clickable, leading to the detailed book page.
 
  - Pagination: Ensure that the book listings are paginated, making it easy to navigate through large numbers of books without overwhelming the user.
 
  - "Want-to-read" Button: Logged-in members can directly add a book to their "Want-to-read" list from the listing page.
 
### Book Detail Page

  - Book Information: Displays comprehensive details about the selected book, including the title, author, genre, publication date, synopsis, and rating.
 
  - "Want-to-read" Button: Allows logged-in users to add the book to their "Want-to-read" list with a single click.
 
  - Reviews Section: Shows reviews from other members, including the reviewer's name, rating, and comment. Logged-in users can leave their own review.
 
  - Navigation Links: Quick links back to the book listings page or Home page

### User Profile Page

  - "Want-to-read" list: This is the primary place where users can view and manage their saved books. When a user logs in and navigates to their profile page, there will be a section called "Want-to-read". This 
    section will display all the books that the user has previously added.

  - Each entry in the list will have buttons to either remove the book from the list or navigate to the book detail page for more information.

  - "Delete Account" Button: When clicked, users will be prompted with a confirmation dialog to ensure they want to proceed with the deletion. Upon confirmation, the user’s account and personal     
    data (e.g. reviews, Want-to-read" list) will be permanently deleted from the database.

  - Users will receive a confirmation message confirming the successful account deletion.

## Future Features 

### Home Page

  - tba

### Book Listing Page

  - tba

### Book Detail Page

  - Related Books: At the bottom of the page, suggest similar or related books based on the genre or author.

### User Profile Page

  - tba

## User Flow Diagrams

<img width="238" alt="book_club_visitor_flowchart_reduced" src="https://github.com/user-attachments/assets/746d33c6-d1bf-4012-ab56-639b6437a6f6">

<img width="408" alt="book_club_member_flowchart_reduced" src="https://github.com/user-attachments/assets/6b1fa831-8b5e-42a5-a173-417e2b8b7b31">

<img width="581" alt="book_club_admin_flowchart_reduced" src="https://github.com/user-attachments/assets/8df23cf0-f69b-4792-b156-69d8bb25c18b">

## Wireframes

### Home Page

![Home_page_wireframes](https://github.com/user-attachments/assets/c8e137cb-ad8c-4b61-813b-a27904722470)

### Book Listing Page

![Book_listing_page_wireframes](https://github.com/user-attachments/assets/8b9fd3ff-4bf6-4b5c-b994-cf97ba9282d1)

### Book Detail Page

tba

### User Profile Page

tba

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

## ER Diagram

![book_club_ER_diagram](https://github.com/user-attachments/assets/ede5057d-209f-4436-b888-4c46f9eabb73)

## Technologies Used

  - Visily
  - Lucidchart
  - Figma
  - MS Word 
 

    
  









