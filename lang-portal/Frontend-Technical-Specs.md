## Frontend Technical Specs

## Pages

### Dashboard /dashboard

#### Purpose

Purpose of this page is to provide a summary of learning progress and act as default page when a user visits the web-app.

#### Components

- Last Study Session
  - last activity used
  - when last activity was used
  - how many words were reviewed
  - how many words were correct
  - how many words were incorrect
- Study Progress
  - total words reviewed
  - mastery progress level displayed as a percentage
- Quick Stats
  - success rate
  - total study sessions
  - time spent studying
  - total active groups
  - study streak
- Start Study Session Button

  - takes us to study activities page

  We need these API endpoints:

- GET /dashboard/last_study_session
- GET /dashboard/study_progress
- GET /dashboard/quick_stats

### Study Activities /study-activities

- List of study activities
- Each study activity has a name and a button
- When a button is clicked, we navigate to the study activity page

#### Purpose

Purpose of this page is to show a collection of study activities that a user can choose from. These will be a thumbnail with name of study activity and a button to start the activity.

#### Components

- name of study activity
- Study Activity Thumbnail
- description of study activity
- button to start the activity
- study activity paginated list
  - id
  - name
  - group name
  - start time
  - end time (inferred by last word_review_item submitted)
  - number of review items
  - button to start the activity

#### Need API endpoints

- GET /api/study-activities/:id
- GET /api/study-activities/:id/study_sessions

### Study Activity Display `/study-activities/:id`

#### Purpose

Purpose of this page is to show the details of a study activity.

#### Components

- Name of study activity
- Thumbnail of study activity
- Description of study activity
- Button to start the activity

#### Need API endpoints

- GET /api/study-activities/:id

### Study Activity Display `/study-activities/:id/sessions/:session_id`

#### Purpose

Launches a new study session for the selected study activity.

#### Components

- Study Activity Name
- Launch form
  - select field for group
  - launch button

#### Behavior

- after launch form is submitted, new tab opens with study activity based on URL in database
- after launch, we navigate to the study session page

#### Need API endpoints

- GET /api/study-activities/:id/sessions/:session_id
- POST /api/study-activities/:id/sessions/:session_id/launch

### Words `/words`

#### Purpose

Purpose of this page is to show a list of all words in database.

#### Components

- word paginated list
  - fields
    - id
    - word
    - group name
    - correct count
    - wrong count
    - button to start the activity
  - 100 items per page

#### Need API endpoints

- GET /api/words

## Word Display `/words/:id`

#### Purpose

Purpose of this page is to show the details of a word.

#### Components

- word details
  - Chinese character
  - Pinyin
  - English definition
  - example sentence
  - example sentence translation
  - audio pronunciation
  - study statistics
    - correct count
    - wrong count
  - word groups

#### Need API endpoints

- GET /api/words/:id

### Word Groups `/word-groups`

#### Purpose

Purpose of this page is to show a list of all word groups in database.

#### Components

- word group paginated list
  - fields
    - id
    - name
    - word count
- clicking on group name navigates to `/word-groups/:id`

#### Need API endpoints

- GET /api/word-groups
