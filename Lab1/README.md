# Lab 1: Requirements Engineering & UML Use-Case Modelling

**Name:** Aanya K | **SRN:** PES2UG24CS011 | **Section:** 5A
**Problem Statement:** #09 - Faculty Research Grant & Publication Tracker

## Files

| File | Purpose |
|------|---------|
| `PES2UG24CS011_Problem_Statement_09.pdf` | The assigned problem statement |
| `PES2UG24CS011_Lab1_Requirements_Table.docx` | 5 functional and 2 non-functional requirements with priority, acceptance criteria, rationale and peer comments |
| `PES2UG24CS011_Lab1_UseCase_Diagram.pdf` | UML use-case diagram |
| `PES2UG24CS011_Lab1_UseCase_Flow.docx` / `.pdf` | One-page flow for the "Submit Publication Record" use case (the PDF is the exported Word file) |

## Requirements

| ID | Summary | Priority |
|----|---------|----------|
| FR-001 | Track grant allocations, log equipment expenses, compute remaining balance | High |
| FR-002 | Faculty Researcher submits a publication record | High |
| FR-003 | Each co-author responds to an approval request | Medium |
| FR-004 | Research Dean records a final Approve/Reject decision | High |
| FR-005 | Scheduled sync of citation counts and indexing status from an external service | Medium |
| NFR-001 | Immutable, tamper-evident audit ledger | High |
| NFR-002 | 95% of requests within 2 seconds at up to 200 concurrent users | Medium |

## Use-case diagram

- **Actors:** Faculty Researcher, Research Dean, Co-Author, Indexing Service (system)
- **Use cases:** UC-01 to UC-08
- **Relationships:** UC-01 Log Grant Expense «include» UC-07 Validate Budget Balance; UC-04 Request Co-Author Approval «extend» UC-03 Submit Publication Record
