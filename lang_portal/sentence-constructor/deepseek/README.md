## DeepSeek-V3 Assistant
Using DeepSeek-V3 to assist with sentence construction for Lang Portal exercise.
### docs
https://platform.openai.com/docs/guides/prompt-engineering

### model
free version (non-local)

# tactics via kaggle
https://www.kaggle.com/code/lonnieqin/prompt-engineering-with-deepseek-chat

# prompting principles
**Principle 1: Write clear and specific instructions**
**Principle 2: Give the model time to “think”**

## Tactics
### Tactic 1: Use delimiters to clearly indicate distinct parts of the input
Delimiters can be anything like: ``, """, < >, ,:`

### Tactic 2: Ask for a structured output
JSON, HTML
```json
[
  {
    "book_id": 1,
    "title": "Whispers of the Forgotten City",
    "author": "Elena M. Hartwell",
    "genre": "Fantasy"
  },
  {
    "book_id": 2,
    "title": "The Quantum Paradox",
    "author": "Dr. James T. Kirk",
    "genre": "Science Fiction"
  },
  {
    "book_id": 3,
    "title": "Beneath the Surface: A Psychological Thriller",
    "author": "Sophia L. Gray",
    "genre": "Thriller"
  }
]
```
### Tactic 3:
- Ask the model to check whether conditions are satisfied


# formatting
no specific formatting requirements via docs
You only need to express who you are + your objective, and that's enough. Especially the background information about who you are — this is extremely useful. The more background information you provide, the better R1 can understand and help you complete tasks. Remember: The best prompting technique is no technique
