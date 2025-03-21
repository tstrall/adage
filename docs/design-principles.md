# 🌐 Core Design Principles

> 🧠 This is not just a list of best practices — it's a fabric of ideas.
>
> Each design principle here supports and complements the others. Together, they form a composable system that allows for flexible, secure, and repeatable deployments across AWS environments. Whether you’re deploying a Lambda function, building out infrastructure, or referencing an external system, the same set of ideas applies.

This project is built on a set of foundational principles that make AWS infrastructure **scalable**, **auditable**, and **developer-friendly**. These principles guide how infrastructure, configuration, and services are defined, deployed, and connected.

---

## 🧱 1. Build Once, Deploy Anywhere  
Terraform modules are reusable and environment-agnostic.  
Each component can be deployed to any environment or AWS account simply by supplying the right configuration — no hardcoded values, no environment-specific logic.

---

## 📦 2. Configuration Is the Source of Truth  
The `aws-config` repository defines what gets deployed and where.  
If a component isn’t represented in configuration (stored in AWS Parameter Store), it won’t be deployed — period.  
Configuration is Git-controlled, making all changes reviewable, trackable, and revertible.

---

## 🔁 3. Immutable Infrastructure  
Infrastructure is replaced, not patched.  
Whether you're updating a service or upgrading a database, you create a new version and cut over to it — no in-place mutations, no snowflake environments.

---

## 🔗 4. Dynamic Dependency Resolution  
Services do not hardcode their dependencies.  
Instead, they reference **nicknames**, and look up runtime details via AWS Parameter Store.  
When a new version of a service is deployed, the runtime parameter is updated — and everything using it gets the new version automatically.

---

## 🧩 5. Separation of Concerns  
Each repo has a single responsibility:  
- `aws-iac`: Infrastructure code (Terraform)  
- `aws-config`: Configuration definitions  
- `aws-lambda`: Application logic & runtime services  
This enables independent testing, deployment, and versioning.

---

## 🌍 6. Environment-Agnostic Components  
Terraform modules receive a nickname and resolve their config from:  
```
/aws/<component>/<nickname>/config
```
...and write their runtime outputs to:  
```
/aws/<component>/<nickname>/runtime
```

No component "knows" whether it’s in dev, qa, or prod — the config defines that.

---

## 🌐 7. External System Referencing  
Systems not built by this infrastructure can still be referenced using predictable config paths like:  
```
/external/<type>/<nickname>/runtime
```
This allows seamless integration with legacy systems or third-party services.

---

## 🔐 8. Git as the Gatekeeper  
All infrastructure and config changes are made via Git.  
If it’s not in version control, it’s not deployed.  
This ensures maximum auditability, security, and traceability.

---

## 💰 9. Flexible, Cost-Conscious Execution  
Terraform components are built to run on both **LocalStack** and **real AWS**.  
This allows developers to test and iterate locally — while keeping AWS costs close to zero during development.

---

## 🧠 10. Optional Caching with Smart Refresh  
To improve performance, services may cache parameter values locally.  
When a failure occurs (e.g., DB disconnect), the system checks Parameter Store again before erroring out — allowing for auto-recovery and real-time rollouts.
