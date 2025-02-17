![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Integrations
Kubernetes
How-to
# Integrating Vercel and Kubernetes
Deploy your frontend on Vercel alongside your existing Kubernetes infrastructure.
Table of Contents
Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications. It has become a popular and powerful way for companies to manage their applications.
You can integrate Vercel with your existing Kubernetes infrastructure to optimizing the delivery of your frontend applications, reducing the number of applications your teams need to support.
Let’s look at key Kubernetes concepts and how Vercel’s managed infrastructure handles them:
  * Server management and provisioning
  * Scaling and redundancy
  * Managing environments and deployments
  * Managing access and security
  * Observability


We'll conclude with how to migrate your frontend from Kubernetes to Vercel.
## Server management and provisioning
With Kubernetes, you must define and configure a web server (e.g. Nginx), resources (CPU, memory), and networking (ingress, API Gateway, firewalls) for each of your nodes and clusters.
Vercel manages server provisioning for you. Through framework-defined infrastructure and support for a wide range of the most popular frontend frameworks, Vercel automatically provisions cloud infrastructure based on your frontend framework code. Vercel also manages every aspect of your domain, including generating, assigning, and renewing SSL certificates.
## Scaling and redundancy
In a self-managed Kubernetes setup, you manually configure your Kubernetes cluster to scale horizontally (replicas) or vertically (resources). It takes careful planning and monitoring to find the right balance between preventing waste (over-provisioning) and causing unintentional bottlenecks (under-provisioning).
In addition to scaling, you may need to deploy your Kubernetes clusters to multiple regions to improve the availability, disaster recovery, and latency of applications.
Vercel automatically scales your applications based on end-user traffic. Vercel deploys your application globally on our Edge Network, reducing latency and improving end-user performance. In the event of regional downtime or an upstream outage, Vercel automatically reroutes your traffic to the next closest region, ensuring your applications are always available to your users.
## Managing environments and deployments
Managing the container lifecycle and promoting environments in a self-managed ecosystem typically involves three parts:
  * Containerization (Docker): Packages applications and their dependencies into containers to ensure consistent environments across development, testing, and production.
  * Container orchestration (Kubernetes): Manages containers (often Docker containers) at scale. Handles deployment, scaling, and networking of containerized applications.
  * Infrastructure as Code (IaC) tool (Terraform): Provisions and manages the infrastructure (cloud, on-premises, or hybrid) in a consistent and repeatable manner using configuration files.


These parts work together by Docker packaging applications into containers, Kubernetes deploying and managing these containers across a cluster of machines, and Terraform provisioning the underlying infrastructure on which Kubernetes itself runs.
An automated or push-button CI/CD process facilities the rollout. Pods are warmed up, a health check is performed to ensure the application is running correctly, and traffic is cut to the new instances.
Vercel knows how to automatically configure your environment through our framework-defined infrastructure, removing the need for containerization, or manually implementing CI/CD for your frontend workload.
Once you connect a Vercel project to a Git repository, every push to a branch automatically creates a new deployment of your application with our git integrations. The default branch (usually `main`) is your production environment. Every time your team pushes to the default branch, Vercel creates a new production deployment. Vercel creates a Preview Deployment when you push to another branch besides the default branch. A Preview Deployment allows your team to test changes and leave feedback using Preview Comments in a live deployment (using a generated URL) before changes are merged to your Git production branch.
Every deploy is immutable, and these generated domains act as pointers. Reverting and deploying is an atomic swap operation. These infrastructure capabilities enable other Vercel features, like Instant Rollbacks and Skew Protection.
## Managing access and security
In a Kubernetes environment, you need to implement security measures such as Role-Based Access Control (RBAC), network policies, secrets management, and environment variables to protect the cluster and its resources by configuring access controls, integrating with existing identity providers (if necessary), and setting up user accounts and permissions. Regular maintenance of the Kubernetes environment is needed for security patches, version updates, and dependency management to defend against vulnerabilities.
With Vercel, you can securely configure environment variables and manage user access, roles, and permissions in the Vercel dashboard. Vercel handles all underlying infrastructure updates and security patches, ensuring your deployment environment is secure and up-to-date.
## Observability
A Kubernetes setup typically uses observability solutions to aid in troubleshooting, alerting, and monitoring of your applications. You could do this through third-party services like Splunk, DataDog, Grafana, and more.
Vercel provides built-in logging and monitoring capabilities through our observability products with real-time logs and built-in traffic analytics. These are all accessible through the Vercel dashboard. If needed, Vercel has one-click integrations with leading observability platforms, so you can keep using your existing tools.
## Migrating from Kubernetes to Vercel
To incrementally move your frontend applications to Vercel:
  1. ### Create a Vercel account and team
Start by creating a Vercel account and team, if needed.
  2. ### Create two versions of your frontend codebase
Keep your current frontend running in Kubernetes for now. Create a fork or a branch of your frontend codebase and connect it to a new Vercel project.
Once connected, Vercel will automatically build and deploy your application. It’s okay if the first deployment fails. View the build logs and troubleshoot the build failures. Changes might include:
     * Adjustments to build scripts
     * Changes to the project configuration
     * Missing environment variables
Continue addressing errors until you get a successful preview deployment.
Depending on how you have your Kubernetes environment configured, you may need to adjust firewall and security policies to allow the applications to talk to each other. Vercel provides some options, including Vercel Secure Compute for Enterprise teams, which allows you to establish secure connections between Vercel and backend environments.
The goal is to use the Preview Deployment to test the integration with your Kubernetes-hosted backends, ensuring that API calls and dataflow work as expected.
  3. ### Setup users and integrations
Use Vercel’s dashboard to securely manage user access, roles, and permissions, so your team can collaborate on the project.
     * Add team members and assign roles (SAML SSO is available on Enterprise plans)
     * Add integrations to any existing services and tools your team uses
  4. ### Begin a full or gradual rollout
Once your preview deployment is passing all tests, and your team is happy with it, you can start to roll it out.
We recommend following our incremental migration guide or our Vercel Adoption guide to help you serve traffic to a Vercel-hosted frontend for any new paths and seamlessly fallback to your existing server for any old paths.
Some other tools or strategies you may want to use:
     * Feature Flags on Vercel
     * A/B Testing on Vercel
     * Implementing Blue-Green Deployments on Vercel
     * Transferring Domains to Vercel
     * How to migrate a site to Vercel without downtime
  5. ### Maintain the backend on Kubernetes
Continue running your backend services on Kubernetes, taking advantage of its strengths in container orchestration for applications your company may not want to move or are unable to move. Examples could include:
     * APIs
     * Remote Procedure Calls (RPC)
     * Change Data Captures (CDC)
     * Extract Transfer Loads (ETL)
Over time, you can evaluate whether specific backend services could also benefit from a serverless architecture and also be migrated to Vercel.
  6. ### Accelerate frontend iteration velocity on Vercel
With Vercel, your development processes become simpler and faster. Vercel combines all the tools you need for CI/CD, staging, testing, feedback, and QA into one streamlined developer experience platform to optimize the delivery of high-quality frontend applications. Instant deployments, live previews, and comments accelerate your feedback cycle, while uniform testing environments ensure the quality of your work. Letting you focus on what you do best: Building top-notch frontend applications.
A recent study found Vercel customers see:
     * Up to 90% increase in site performance
     * Up to 80% reduction in time spent deploying
     * Up to 4x faster time to market


## Behind the scenes of Vercel's infrastructure
If you want to understand how Vercel builds and deploys serverless applications for maximum scalability, performance, and fast iterations, you can learn more in the Behind the scenes of Vercel's infrastructure blog post.
Last updated on July 23, 2024
Previous
Sign in with Vercel
Was this helpful?
supported.
Send
AskAsk v0
KubernetesAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
