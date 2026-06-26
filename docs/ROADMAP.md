# ROADMAP.md

## Roadmap for SaaS Visibility Guard

### MVP Milestone

The Minimum Viable Product (MVP) for SaaS Visibility Guard focuses on delivering core functionality that allows users to export SaaS usage and risk scores as a CSV file. This will ensure that the product meets the basic requirements for launch and provides value to early adopters.

#### MVP-Critical Features:

- **Core Functionality**
  - Implement `SaaSVisibilityGuard` class with initialization accepting a list of `SaaSUsage` objects. (MVP-Critical)
  - Develop `export_csv` method to generate a CSV string from provided `SaaSUsage` data. (MVP-Critical)
  - Create `get_saas_usage` method to retrieve a list of `SaaSUsage` objects. (MVP-Critical)

- **Testing**
  - Set up pytest framework for testing. (MVP-Critical)
  - Write unit tests covering all methods within `SaaSVisibilityGuard`. (MVP-Critical)

### Version 1 Phase

Building upon the MVP, Version 1 aims to enhance user experience and expand the capabilities of SaaS Visibility Guard.

#### Themes:

- **Enhanced Data Handling**
  - Add support for additional data formats such as JSON and Excel. 
  - Implement error handling for invalid or corrupted input data.

- **Advanced Analytics**
  - Introduce basic analytics features to provide insights into SaaS usage patterns.
  - Develop a dashboard interface for visualizing key metrics.

### Version 2 Phase

Version 2 focuses on integrating advanced features and improving scalability to cater to larger enterprises.

#### Themes:

- **Scalability and Performance**
  - Optimize code for better performance with large datasets.
  - Implement caching mechanisms to reduce processing time.

- **Enterprise Integration**
  - Develop APIs for seamless integration with enterprise systems.
  - Add support for multi-tenant environments.

### Detailed Breakdown

#### MVP Milestone

- **Core Functionality**
  - Initialize `SaaSVisibilityGuard` class with a constructor that accepts a list of `SaaSUsage` objects.
  - Implement `export_csv` method to convert `SaaSUsage` data into a well-formatted CSV string.
  - Create `get_saas_usage` method to fetch and return a list of `SaaSUsage` objects based on specified criteria.

- **Testing**
  - Set up pytest environment and write comprehensive unit tests for all implemented methods.
  - Ensure test coverage includes edge cases and potential failure scenarios.

#### Version 1 Phase

- **Enhanced Data Handling**
  - Extend `export_csv` method to include options for exporting data in JSON and Excel formats.
  - Implement robust error handling to manage issues like invalid data types or corrupted files.

- **Advanced Analytics**
  - Integrate basic analytics functions to calculate and display usage trends and risk scores.
  - Design a simple dashboard interface using a lightweight web framework like Flask.

#### Version 2 Phase

- **Scalability and Performance**
  - Refactor code to optimize performance, especially when dealing with large volumes of data.
  - Introduce caching strategies to minimize redundant computations and speed up data retrieval.

- **Enterprise Integration**
  - Develop RESTful APIs to facilitate integration with various enterprise applications.
  - Enhance architecture to support multi-tenant configurations, ensuring data isolation and security.

This roadmap outlines a clear path for the evolution of SaaS Visibility Guard, starting from a functional MVP and progressing towards a feature-rich, scalable solution tailored for enterprise needs.
