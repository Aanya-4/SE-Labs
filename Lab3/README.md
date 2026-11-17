# Lab 3: Component Modelling & Architectural Pattern Selection

**Name:** Aanya K | **SRN:** PES2UG24CS011 | **Section:** 5A
**Problem Statement:** #09 - Faculty Research Grant & Publication Tracker

## Files

| File | Purpose |
|------|---------|
| `PES2UG24CS011_Problem_Statement_09.pdf` | The assigned problem statement |
| `PES2UG24CS011_Lab3_Component_Diagram.png` | UML component diagram |
| `PES2UG24CS011_Lab3_Justification.docx` / `.pdf` | One-page architecture justification |
| `PES2UG24CS011_Lab3_Full_Submission.pdf` | Complete document: style analysis, components, diagram, interfaces and justification |

## Architecture

**Layered architecture** (Presentation / Business / Data), chosen over microservices and client-server.

| Layer | Component |
|-------|-----------|
| Presentation | Portal UI |
| Business | Workflow Manager, Audit Ledger, Metrics Sync Connector |
| Data | Database |
| External | Indexing Service |

## Interfaces

| Provided by | Interface | Required by |
|-------------|-----------|-------------|
| Workflow Manager | ManageRequest | Portal UI |
| Audit Ledger | AuditLog | Workflow Manager |
| Database | DataAccess | Workflow Manager |
| Database | LedgerPersist | Audit Ledger |
| Database | MetricsWrite | Metrics Sync Connector |
| Indexing Service (external) | IndexingQuery | Metrics Sync Connector |
