---
platform: ChatGPT
title: Skoobe Hetzner Migration Engineer
description: Migration Engineering session
model_customizations:
  system_message: You are an expert artificial intelligence prompt engineer, with the ability to assist users in iteratively improving prompts.
---

I want you to become my Hetzner Migration Engineer

Your goal is to help me successfully migrate our services from AWS to Hetzner. The prompt will be used by you, {{ platform }}.

Generate a prompt to act like an expert on the migration of the internal applications of a book industry web and mobile app provider from AWS to the German Cloud Provider Hetzner. Ensure a detailed plan is considered. Only 1-2 hours downtime is permissible.
The Company's Applications / Web solutions are:
  Hub: Content Categorisation; Ingestion of Books from Publishers; 
    Pipelines for:
        1. Book Intake:
            1.1 Components for the Ingestion of Books Packages from Publishers 
                1.1.1 a Book Package from a Publisher consisting of: 
                    a. an epub file
                    b. the industry standard .xml files (known as an 'Onix')
                    c. and an image for display as the book cover. 
        2. EPub Content Pipeline
            2.1 IP Protection: Encryption of Book Chapters
            2.2 Scaling and Modification of Images
        3. Audiobook Content
            3.1 Delivery of .flac files to a Technical Partner for conversion to .mp4 format
        4. Book Categorisation
            4.1 Assignmnent of a Book to a Category/Categories
            4.2 Tagging of Books with Keywords
            4.3 Any special Marketing promotion of a Book
        5. Book Deployment (to a User facing system: Services)
            5.1 Book Deployment is a key Business Process that involves the weekly release of 300-500 books to the Services App
 
    Technical Stack: 
        MySQL 5.8
        Python Services exposing a number of Internal API endpoints
        An internal UI
  Services: The User Facing System
    Key Use Cases
        1. Serve Content to Mobile Apps:
            1.1 IOS
            1.2 Android
            1.3 EBook Readers
        2. Ingest Date from End Users:
            Reading Time Data (Page Flips, Words read; page dwell period )
            Audiobook Listening Data
        3. Co-ordinate the Borrowing / Returning of Books from EPub Readers
    Technical Stack: 
        MySQL 5.8
        Java Services exposing a number of External API endpoints
        Python Services
        Hazelcast
        GraphQL
  Website:
    1. Landing Pages
    2. Selection of available Book Catalogue
    3. Membership and Subscription Management
  Sales Reports:
    1. Reports to Publishers on Revenue earned from their books on the Platform for previous month
  Accounts:
    1. Subscription Managment
    2. Subscription Renewal

all of these are currently hosted on Amazon Web Services. 
Nomad is used as a Job Scheduler and Cluster Manager