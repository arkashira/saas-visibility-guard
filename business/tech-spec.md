# Tech Spec
## Stack
* Language: Python 3.10
* Framework: FastAPI 0.92.0
* Runtime: Uvicorn 0.18.3 with Gunicorn 20.1.0

## Hosting
* Primary Platform: AWS (free tier eligible)
* Secondary Platform: Google Cloud Platform (free tier eligible)
* Containerization: Docker 20.10.17
* Orchestration: Kubernetes 1.24.3 (optional)

## Data Model
The following tables/collections will be used to store data:
* **saas_applications**
	+ id (primary key, UUID)
	+ name (string)
	+ description (string)
	+ url (string)
* **msp_accounts**
	+ id (primary key, UUID)
	+ name (string)
	+ email (string)
	+ password (hashed string)
* **saas_usage**
	+ id (primary key, UUID)
	+ saas_application_id (foreign key referencing saas_applications.id)
	+ msp_account_id (foreign key referencing msp_accounts.id)
	+ usage_date (date)
	+ usage_count (integer)
* **user_sessions**
	+ id (primary key, UUID)
	+ msp_account_id (foreign key referencing msp_accounts.id)
	+ session_start (datetime)
	+ session_end (datetime)

## API Surface
The following endpoints will be exposed:
### Authentication
* **POST /login**: Authenticate a user and return a JSON Web Token (JWT)
	+ Method: POST
	+ Path: /login
	+ Purpose: Authenticate a user
	+ Request Body: { email: string, password: string }
	+ Response: { token: string }
* **POST /logout**: Invalidate a user's JWT
	+ Method: POST
	+ Path: /logout
	+ Purpose: Invalidate a user's JWT
	+ Request Body: { token: string }
	+ Response: { success: boolean }
### SaaS Applications
* **GET /saas-applications**: Retrieve a list of all SaaS applications
	+ Method: GET
	+ Path: /saas-applications
	+ Purpose: Retrieve a list of all SaaS applications
	+ Response: [{ id: UUID, name: string, description: string, url: string }]
* **POST /saas-applications**: Create a new SaaS application
	+ Method: POST
	+ Path: /saas-applications
	+ Purpose: Create a new SaaS application
	+ Request Body: { name: string, description: string, url: string }
	+ Response: { id: UUID, name: string, description: string, url: string }
* **GET /saas-applications/{id}**: Retrieve a SaaS application by ID
	+ Method: GET
	+ Path: /saas-applications/{id}
	+ Purpose: Retrieve a SaaS application by ID
	+ Response: { id: UUID, name: string, description: string, url: string }
* **PUT /saas-applications/{id}**: Update a SaaS application
	+ Method: PUT
	+ Path: /saas-applications/{id}
	+ Purpose: Update a SaaS application
	+ Request Body: { name: string, description: string, url: string }
	+ Response: { id: UUID, name: string, description: string, url: string }
* **DELETE /saas-applications/{id}**: Delete a SaaS application
	+ Method: DELETE
	+ Path: /saas-applications/{id}
	+ Purpose: Delete a SaaS application
	+ Response: { success: boolean }
### SaaS Usage
* **GET /saas-usage**: Retrieve a list of all SaaS usage
	+ Method: GET
	+ Path: /saas-usage
	+ Purpose: Retrieve a list of all SaaS usage
	+ Response: [{ id: UUID, saas_application_id: UUID, msp_account_id: UUID, usage_date: date, usage_count: integer }]
* **POST /saas-usage**: Create a new SaaS usage entry
	+ Method: POST
	+ Path: /saas-usage
	+ Purpose: Create a new SaaS usage entry
	+ Request Body: { saas_application_id: UUID, msp_account_id: UUID, usage_date: date, usage_count: integer }
	+ Response: { id: UUID, saas_application_id: UUID, msp_account_id: UUID, usage_date: date, usage_count: integer }

## Security Model
* Authentication: JSON Web Tokens (JWT) with HS256 signing
* Authorization: Role-Based Access Control (RBAC) with the following roles:
	+ Admin: Full access to all endpoints
	+ MSP: Read-only access to SaaS applications and usage data
* Secrets Management: AWS Secrets Manager
* IAM: AWS IAM with the following policies:
	+ Admin: Full access to all resources
	+ MSP: Read-only access to SaaS applications and usage data

## Observability
* Logging: AWS CloudWatch Logs
* Metrics: AWS CloudWatch Metrics
* Tracing: AWS X-Ray

## Build/CI
* Build Tool: Docker 20.10.17
* CI Tool: GitHub Actions 2.293.0
* CD Tool: AWS CodeDeploy 1.4.2
* Testing Framework: Pytest 6.2.5
* Linting Tool: Black 22.3.0
* Code Formatter: Black 22.3.0
* Code Analyzer: Bandit 1.7.1
* Security Scanner: Safety 2.0.0