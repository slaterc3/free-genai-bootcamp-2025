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

# Database Schema

## Tables

### words — Stores individual Japanese vocabulary words.

- `id` (Primary Key): Unique identifier for each word
- `kanji` (String, Required): The word written in Japanese kanji
- `romaji` (String, Required): Romanized version of the word
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
