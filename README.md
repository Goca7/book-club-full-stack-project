<h1 align="center">Page Turners</h1>

Page Turners aims to provide an engaging and user-friendly platform for adult readers to discover and review books. The platform is designed for book enthusiasts who want to explore book details, save their favorite titles for future reading, and contribute to the community by leaving reviews. The target audience primarily consists of adult readers seeking to connect with like-minded individuals through book reviews. The site also provides functionality for admins to manage content efficiently, including the ability to moderate reviews and maintain the book database. 

[View the live project here] (https://

## Table of Contents (tba)

## User Stories

#### User Story: User Sign-Up
- As a visitor, I want to sign up easily, so that I can join the Book Club.

- Acceptance Criteria:

  1. The sign-up form should have fields for username and password.

  2. Form validation must ensure that usernames are unique and in a valid format.

#### User Story: View Book Details
- As a visitor, I want to sign up easily, so that I can join the Book Club.

- Acceptance Criteria:

  1. Visitors should be able to click on a book title to view its details (title, author, genre, description).

  2. The book detail page must include user reviews and ratings.

  3. Non-members must have access to view book details without logging in.

#### User Story: Secure Login
- As a member, I want to view book details, so that I can learn more about specific titles before deciding to read them.

- Acceptance Criteria:

  1. The data entered by the user into the login form (username and password) is correct and in the proper format before it is submitted to the server for processing.
  
#### User Story: Leave Review  
- As a member, I want to leave reviews for books I have read, so that I can share my opinions with other.

- Acceptance Criteria:

    1. Users must be logged in to submit a review.

    2. Reviews should be displayed with the user's name, rating (1–5 stars), and review text.

    3. Users must have the option to edit or delete their reviews.

#### User Story: Add Books to "Want-to-read" List
- As a member, I want to add books to my "Want-to-read" list, so that I can save books for future reading.

- Acceptance Criteria:

  1. Users should have an "Want-to-read" button on each book detail page.

  2. The system must store the list under the user's profile and be accessible at any time.

  3. Users should have the ability to remove books from their "Want-to-read" list.

#### User Story: Receive Notifications
- As a member, I want to receive notifications about my submissions, so that I know they were properly recorded.

- Acceptance Criteria:

  1. The system should send a notification when a user submits a book review.
 
#### User Story: Account Deletion
- As a member, I want to delete my account easily, so that I can remove my personal data and stop using the platform.

- Acceptance Criteria:

  1. The user can navigate to the profile page and find a "Delete Account" button.

  2. Upon clicking the button, a confirmation prompt appears, asking the user to confirm the deletion.

  3. The system permanently deletes the user’s account and associated data (e.g., reviews, "Want-to-read" list) upon confirmation.

  4. The user receives a confirmation message notifying them that their account has been deleted.

  5. After deletion, the user can no longer log in with the deleted account credentials.

#### User Story: Review Moderation
- As an admin, I want to view and moderate members' reviews, so that I can ensure they are appropriate.
  
- Acceptance Criteria:

  1. Admins should be able to access a dashboard to see all user reviews and comments.

  2. Admins must have the ability to delete inappropriate content.

#### User Story: Manage Database
- As an admin, I want to add, edit, and delete books from the database, so that I can manage the content of the site.

- Acceptance Criteria:

  1. Admins should be able to create new book entries through a form.

  2. Admins must be able to edit book information like title, author, genre, and description.

  3. Admins must have the ability to delete books and their associated data.
 
## Existing Features

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
 
  - Related Books: At the bottom of the page, suggest similar or related books based on the genre or author.
 
  - Navigation Links: Quick links back to the book listings page or Home page

### User Profile Page

  - "Want-to-read" list: This is the primary place where users can view and manage their saved books. When a user logs in and navigates to their profile page, there will be a section called "Want-to-read". This 
    section will display all the books that the user has previously added.

  - Each entry in the list will have buttons to either remove the book from the list or navigate to the book detail page for more information.

  - "Delete Account" Button: When clicked, users will be prompted with a confirmation dialog to ensure they want to proceed with the deletion. Upon confirmation, the user’s account and personal     
    data (e.g. reviews, Want-to-read" list) will be permanently deleted from the database.

  - Users will receive a confirmation message confirming the successful account deletion.

## Future Features (tba)

## User Flow Diagrams

<img width="238" alt="book_club_visitor_flowchart_reduced" src="https://github.com/user-attachments/assets/746d33c6-d1bf-4012-ab56-639b6437a6f6">

<img width="408" alt="book_club_member_flowchart_reduced" src="https://github.com/user-attachments/assets/6b1fa831-8b5e-42a5-a173-417e2b8b7b31">

<img width="581" alt="book_club_admin_flowchart_reduced" src="https://github.com/user-attachments/assets/8df23cf0-f69b-4792-b156-69d8bb25c18b">

## Technologies Used

  - UI Design Software for User Flow Diagrams
    https://www.visily.ai/

    
  









