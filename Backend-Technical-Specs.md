# Language Learning Portal Backend Server Technical Specifications

## Business Goal

The goal is to build a prototype of a language learning portal that serves three main purposes:

1. **Vocabulary Inventory Management**

   - Act as a comprehensive repository of learnable vocabulary
   - Maintain organized collections of words and phrases

2. **Learning Record Store (LRS)**

   - Track student performance metrics
   - Store correct and incorrect scores for vocabulary practice
   - Monitor learning progress over time

3. **Unified Learning Platform**
   - Serve as a central launchpad for various learning applications
   - Provide seamless integration between different learning tools
   - Enable consistent user experience across learning activities

## System Overview

This portal will integrate these three core functionalities to create a comprehensive language learning ecosystem that supports both teachers and students in the learning process.

---

_Note: This is a living document and will be updated as specifications evolve._

# Technical Requirements

- backend server will be built with Flask
- database will be built with SQLite
- the API will be built with OpenAPI
- API will return JSON data
- AWS RDS will be used for database
- AWS S3 will be used for media storage
- AWS Lambda will be used for background tasks
- AWS API Gateway will be used for API management
- AWS CloudWatch will be used for monitoring
- AWS CloudFormation will be used for infrastructure as code
- AWS IAM will be used for authentication
- AWS Route 53 will be used for DNS
- AWS Certificate Manager will be used for SSL/TLS certificates

# Database Schema

## Tables

### words — Stores individual Japanese vocabulary words.

- `id` (Primary Key): Unique identifier for each word
- `characters` (String, Required): The word written in Traditional Chinese characters
- `pinyin` (String, Required): Romanized pronunciation of the word
- `english` (String, Required): English translation of the word
- `parts` (JSON, Required): Word components stored in JSON format

### groups — Manages collections of words.

- `id` (Primary Key): Unique identifier for each group
- `name` (String, Required): Name of the group
- `words_count` (Integer, Default: 0): Counter cache for the number of words in the group

### word_groups — join-table enabling many-to-many relationship between words and groups.

- `word_id` (Foreign Key): References words.id
- `group_id` (Foreign Key): References groups.id

### study_activities — Defines different types of study activities available.

- `id` (Primary Key): Unique identifier for each activity
- `name` (String, Required): Name of the activity (e.g., "Flashcards", "Quiz")
- `url` (String, Required): The full URL of the study activity
- `created_at` (Timestamp, Default: Current Time): When the activity was created

### study_sessions — Records individual study sessions.

- `id` (Primary Key): Unique identifier for each session
- `group_id` (Foreign Key): References groups.id
- `study_activity_id` (Foreign Key): References study_activities.id
- `created_at` (Timestamp, Default: Current Time): When the session was created

### word_review_items — Tracks individual word reviews within study sessions.

- `id` (Primary Key): Unique identifier for each review
- `word_id` (Foreign Key): References words.id
- `study_session_id` (Foreign Key): References study_sessions.id
- `correct` (Boolean, Required): Whether the answer was correct
- `created_at` (Timestamp, Default: Current Time): When the review occurred

## Relationships

Relationships

- word belongs to groups through word_groups
- group belongs to words through word_groups
- session belongs to a group
- session belongs to a study_activity
- session has many word_review_items
- word_review_item belongs to a study_session
- word_review_item belongs to a word

### API Endpoints

- GET /api/study-activities/:id
- GET /api/study-activities/:id/sessions
- GET /api/dashboard/last_study_session
- GET /api/dashboard/study_progress

- GET /api/words
  - pagination with 100 items per page
- GET /api/words/:id
- GET /api/word-groups
  - pagination with 10 items per page
- GET /api/word-groups/:id
- GET /api/word-groups/:id/words

- GET /api/study-activities/:id
- GET /api/study-activities/:id/study_sessions

- GET /api/study-activities/:id/sessions/:session_id
- POST /api/study-activities/:id/sessions/:session_id/launch
  - required parameters:
    - group_id, study_activity_id
