Skip to content
Menu
On this page
# Traefik Proxy ​
Traefik ↗ is a modern, open-source reverse proxy and load balancer designed to handle incoming requests and route them to the appropriate services. It’s widely used in the container ecosystem, making it a perfect fit for projects running on Coolify.
By default, Coolify uses Traefik as its proxy, enabling easy management of routing, SSL certificates, and more, without requiring deep technical expertise.
## Why Use Traefik? ​
  * Dynamically manages routing between your apps and the internet.
  * Integrates seamlessly with container orchestrators like Docker or Kubernetes.
  * Simplifies SSL/TLS certificate management, including support for Let's Encrypt ↗.
  * Offers advanced features like load balancing and middleware for fine-grained control.
  * Comes with a built-in dashboard for monitoring routes and configurations.


## When Not to Use Traefik? ​
  * If you need complete control over every aspect of your reverse proxy.
  * If you prefer using another reverse proxy solution like NGINX ↗.
  * If you have highly customized or complex routing rules that Traefik might not fully support.


## Ways to Use Traefik with Coolify ​
Coolify automatically configures Traefik as your proxy. However, you can customize and extend Traefik's functionality based on your needs.
Below are some of the key features and ways you can use Traefik with Coolify:
  1. Basic Authentication -> Add username and password protection to your applications.
  2. Custom SSL Certificates -> Use your own SSL certificates instead of automatically generated ones.
  3. Dashboard -> Enable Traefik’s built-in dashboard for real-time monitoring and insights.
  4. Dynamic Configuration -> Manage dynamic configuration changes like routing rules or middlewares.
  5. Health Checks -> Configure health checks to ensure your applications are running smoothly.
  6. Load Balancing -> Distribute traffic across multiple app instances for better performance.
  7. Redirects -> Set up HTTP-to-HTTPS redirection or create specific URL redirects.
  8. Wildcard Certificates -> Secure multiple subdomains with a single SSL certificate.


CAUTION!
**Do not make changes to Traefik's configuration unless you are sure of what you are doing. Incorrect settings can make your entire application inaccessible..**
**We highly recommend testing any changes in a development environment before applying them to production.**
