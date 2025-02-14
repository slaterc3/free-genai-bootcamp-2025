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
- database will be built with PostgreSQL
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

Our database will be built with PostgreSQL called `lang_portal.db` that will be in the root of the project folder of `backend_python`.
We have the following tables:

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

#### GET /api/study-activities/:id

Returns information about a study activity.

```json
{
  "id": 1,
  "group_id": 1,
  "group_name": "Passive Sentences",
  "name": "Flashcards",
  "study_activity_id": 1,
  "url": "https://flashcards.example.com",
  "created_at": "2024-03-20T10:00:00Z"
}
```

#### GET /api/study-activities/:id/sessions

Returns all study sessions for a given study activity.

```json
{
  "sessions": [
    {
      "id": 1,
      "group_id": 123,
      "study_activity_id": 1,
      "created_at": "2024-03-20T10:00:00Z",
      "correct_count": 15,
      "total_reviews": 20
    }
  ]
}
```

#### GET /api/dashboard/last_study_session

Returns the last study session for the user.

```json
{
  "session": {
    "id": 1,
    "group_id": 123,
    "study_activity_id": 1,
    "created_at": "2024-03-20T10:00:00Z",
    "group_name": "Basic Vocabulary",
    "activity_name": "Flashcards"
  }
}
```

#### GET /api/dashboard/study_progress

Returns the study progress for the user.

```json
{
  "daily_stats": [
    {
      "date": "2024-03-20",
      "correct_count": 25,
      "total_reviews": 30
    }
  ],
  "total_words_studied": 150,
  "average_accuracy": 0.85
}
```

- GET /api/words

  - pagination with 100 items per page
    ```json
    {
      "words": [
        {
          "id": 1,
          "characters": "你好",
          "pinyin": "nǐ hǎo",
          "english": "hello",
          "parts": {
            "characters": ["你", "好"],
            "pinyin": ["nǐ", "hǎo"]
          }
        }
      ],
      "pagination": {
        "current_page": 1,
        "total_pages": 10,
        "total_items": 1000,
        "items_per_page": 100
      }
    }
    ```

  ```

  ```

- GET /api/words/:id
- GET /api/words/:id
  ```json
  {
    "id": 1,
    "characters": "你好",
    "pinyin": "nǐ hǎo",
    "english": "hello",
    "parts": {
      "characters": ["你", "好"],
      "pinyin": ["nǐ", "hǎo"]
    }
  }
  ```
- GET /api/word-groups

  - pagination with 10 items per page

  ```json
  {
    "groups": [
      {
        "id": 1,
        "name": "Basic Vocabulary",
        "words_count": 50
      }
    ],
    "pagination": {
      "current_page": 1,
      "total_pages": 5,
      "total_items": 50,
      "items_per_page": 10
    }
  }
  ```

- GET /api/word-groups/:id
  ```json
  {
    "id": 1,
    "name": "Basic Vocabulary",
    "words_count": 50
  }
  ```
- GET /api/word-groups/:id/words
  ```json
  {
    "group_id": 1,
    "group_name": "Basic Vocabulary",
    "words": [
      {
        "id": 1,
        "characters": "你好",
        "pinyin": "nǐ hǎo",
        "english": "hello",
        "parts": {
          "characters": ["你", "好"],
          "pinyin": ["nǐ", "hǎo"]
        }
      }
    ]
  }
  ```
- GET /api/study-activities/:id

- GET /api/study-activities/:id/study_sessions
  ```json
  {
    "group_id": 1,
    "sessions": [
      {
        "id": 1,
        "study_activity_id": 1,
        "activity_name": "Flashcards",
        "created_at": "2024-03-20T10:00:00Z",
        "correct_count": 15,
        "total_reviews": 20
      }
    ]
  }
  ```
- GET /api/study-activities/:id/sessions/:session_id
  ```json
  {
    "session_id": 1,
    "group_id": 123,
    "study_activity_id": 1,
    "created_at": "2024-03-20T10:00:00Z",
    "reviews": [
      {
        "word_id": 1,
        "correct": true,
        "created_at": "2024-03-20T10:01:00Z"
      }
    ]
  }
  ```
- POST /api/study-activities/:id/sessions/:session_id/launch

```json
{
  "session_id": 1,
  "group_id": 123,
  "study_activity_id": 1,
  "redirect_url": "https://flashcards.example.com/session/1"
}
```

- required parameters:

  - session_id, group_id, study_activity_id

-

- GET /api/settings

```json
{
  "daily_goal": 50,
  "preferred_activity_id": 1,
  "notifications_enabled": true
}
```

- POST /api/settings
  ```json
  {
    "success": true,
    "settings": {
      "daily_goal": 50,
      "preferred_activity_id": 1,
      "notifications_enabled": true
    }
  }
  ```
- POST /api/settings/reset-history

```json
{
  "success": true,
  "reset_at": "2024-03-20T10:00:00Z"
}
```

- POST /api/study_sessions/:id/words/word_id/review
  - required parameters:
    - correct
  ```json
  {
    "success": true,
    "review": {
      "word_id": 1,
      "correct": true,
      "created_at": "2024-03-20T10:00:00Z"
    },
    "session_stats": {
      "correct_count": 16,
      "total_reviews": 21
    }
  }
  ```

## Invoke Tasks

Invoke is a tool for running tasks in a project.
Here are tasks for lang portal that we need to run:

### Initialize Database

This will initialize the postgres database called `lang_portal.db` in the root of the project folder of `backend_python`.

```bash
invoke init-db
```

### Migrate Database

This will migrate the database to the latest version.
Migrations are in the `lang_portal/migrations` folder.
The file name should look like `V001__create_words_table.py`

```bash
invoke migrate-db
```

### Seed Data

This task will import json files and transform them into the database tables.
All seed files are in the `lang_portal/data/seed` folder.
All seed files should be loaded in alphabetical order.
we will have yaml files for seed files that will have the following format:

```yaml
- model: app.models.Word
  data:
    - characters: 你好
      pinyin: nǐ hǎo
      english: hello
      parts:
        characters: ["你", "好"]
        pinyin: ["nǐ", "hǎo"]
```

```bash
invoke seed-data
```
