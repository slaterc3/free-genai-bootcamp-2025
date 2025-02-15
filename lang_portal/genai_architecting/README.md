# Language Learning Application

## Functional Requirements

1. **User Registration and Authentication**

   - Users can be learners, teachers or guests
   - Mechanism for sign-up, login, authentication

2. **Language Activities**

   - Provide interactive activities, including:
     - Sentence Construction
     - Vocabulary Warmups
     - Dialogue Building
     - Pronunciation Practice
     - Writing Practice

3. **Linguistic Repository Integration**

   - Retrieve core vocabulary, grammar rules, and native speaker examples from the database.

4. **Dynamic Content Personalization**

   - Retrieve personalized activities and suggestions using the Retriever Agent (RAG) and the DuckDB vector database.

5. **Sentence Constructor Workflow**

   - Allow users to input queries into the Sentence Constructor, preprocess them, and generate outputs using the LLM

6. **Frontend Interface**

   - Enable users to interact with the app via a React-based frontend, displaying activities and progress.

7. **Data Caching**

   - Implement prompt caching to reduce latency for users

8. **AI PC**
   - Invest in AI PC so that LLM can run locally

---

## Non-Functional Requirements

1. **Performance**

   - Ensure query-response time does not exceed 2 seconds for common activities.

2. **Scalability**

   - The system should support up to 10,000 concurrent users without degradation in performance.

3. **Reliability**

   - Maintain 99.9% uptime for the Lang Portal and activity modules.

4. **Security**

   - Protect user data with end-to-end encryption and secure authentication mechanisms (e.g., OAuth2).

5. **Maintainability**

   - Use modular components (e.g., DuckDB, LLM, Retriever Agent) for ease of updates and debugging.

6. **Usability**

   - The React frontend should provide a clean and intuitive user interface for all user types (learners and teachers).

7. **Compatibility**

   - Ensure the system integrates seamlessly with existing cloud services (e.g., OpenAI GPT-4, DuckDB) and supports future LLM upgrades.

8. **Localization**
   - Support multilingual UI options, starting with English and Chinese.

## Data Considerations

1. **Data Collection and Storage**
2. **Data Privacy and Security**

## Model Selection and Development

- Choose appropriate models based on your use cases. Consider factors such as:
- Self Hosted vs SaaS
- Open weight vs Open Source
- Input-Output: text-to-text?
- Number of models needed
- Number of calls/model
- Size
- Evaluation
- Context window: input, output
- Fine-tuning requirements
- Model performance and efficiency

## Infrastructure Design

**Design a scalable and flexible infrastructure**

- that can support GenAI workloads
- Leverage cloud platforms for scalability/hardware

## Integration and Deployment

**seamless integration with existing systems**

- Develop APIs and interfaces (accessing GenAI)
- CI/CD pipeline for deployment/monitoring

## Monitoring and Optimization

- Robust Logging for errors/auditability
- Develop KPIs
