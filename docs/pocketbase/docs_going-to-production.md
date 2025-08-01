Going to production
###  Deployment strategies 
#####  Minimal setup 
One of the best PocketBase features is that it's completely portable. This mean that it doesn't require any external dependency and **could be deployed by just uploading the executable on your server**.
Here is an example for starting a production HTTPS server (auto managed TLS with Let's Encrypt) on clean Ubuntu 22.04 installation.
  1. Consider the following app directory structure:
`myapp/   pb_migrations/   pb_hooks/   pocketbase`
  2. Upload the binary and anything else required by your application to your remote server, for example using **rsync** :
`rsync -avz -e ssh /local/path/to/myapp root@YOUR_SERVER_IP:/root/pb`
  3. Start a SSH session with your server:
`ssh root@YOUR_SERVER_IP`
  4. Start the executable (specifying a domain name will issue a Let's encrypt certificate for it)
`[root@dev ~]$ /root/pb/pocketbase serve yourdomain.com`
> Notice that in the above example we are logged in as **root** which allow us to bind to the **privileged 80 and 443 ports**. For **non-root** users usually you'll need special privileges to be able to do that. You have several options depending on your OS - `authbind`, `setcap`, `iptables`, `sysctl`, etc. Here is an example using `setcap`:
> `[myuser@dev ~]$ sudo setcap 'cap_net_bind_service=+ep' /root/pb/pocketbase`
  5. (Optional) Systemd service
You can skip step 3 and create a **Systemd service** to allow your application to start/restart on its own. Here is an example service file (usually created in `/lib/systemd/system/pocketbase.service`):
`[Unit] Description = pocketbase [Service] Type       = simple User       = root Group      = root LimitNOFILE   = 4096 Restart     = always RestartSec    = 5s StandardOutput  = append:/root/pb/std.log StandardError  = append:/root/pb/std.log WorkingDirectory = /root/pb ExecStart    = /root/pb/pocketbase serve yourdomain.com [Install] WantedBy = multi-user.target`
After that we just have to enable it and start the service using `systemctl`:
`[root@dev ~]$ systemctl enable pocketbase.service [root@dev ~]$ systemctl start pocketbase`
> You can find a link to the Web UI installer in the `/root/pb/std.log`, but alternatively you can also create the first superuser explicitly via the `superuser` PocketBase command:
> `[root@dev ~]$ /root/pb/pocketbase superuser create EMAIL PASS`


#####  Using reverse proxy 
If you plan hosting multiple applications on a single server or need finer network controls, you can always put PocketBase behind a reverse proxy such as _NGINX_ , _Apache_ , _Caddy_ , etc. _Just note that when using a reverse proxy you may need to setup the "User IP proxy headers" in the PocketBase settings so that the application can extract and log the actual visitor/client IP (the headers are usually`X-Real-IP` , `X-Forwarded-For`)._
Here is a minimal _NGINX_ example configuration:
`server {   listen 80;   server_name example.com;   client_max_body_size 10M;   location / {     # check http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive     proxy_set_header Connection '';     proxy_http_version 1.1;     proxy_read_timeout 360s;     proxy_set_header Host $host;     proxy_set_header X-Real-IP $remote_addr;     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;     proxy_set_header X-Forwarded-Proto $scheme;     # enable if you are serving under a subpath location     # rewrite /yourSubpath/(.*) /$1 break;     proxy_pass http://127.0.0.1:8090;   } }`
Corresponding _Caddy_ configuration is:
`example.com {   request_body {     max_size 10MB   }   reverse_proxy 127.0.0.1:8090 {     transport http {       read_timeout 360s     }   } }`
#####  Using Docker 
Some hosts (e.g. fly.io) use Docker for deployments. PocketBase doesn't have an official Docker image, but you could use the below minimal Dockerfile as an example:
`FROM alpine:latest ARG PB_VERSION=0.29.0 RUN apk add --no-cache \   unzip \   ca-certificates # download and unzip PocketBase ADD https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip /tmp/pb.zip RUN unzip /tmp/pb.zip -d /pb/ # uncomment to copy the local pb_migrations dir into the image # COPY ./pb_migrations /pb/pb_migrations # uncomment to copy the local pb_hooks dir into the image # COPY ./pb_hooks /pb/pb_hooks EXPOSE 8080 # start PocketBase CMD ["/pb/pocketbase", "serve", "--http=0.0.0.0:8080"]`
To persist your data you need to mount a volume at `/pb/pb_data`.
_For a full example you could check the"Host for free on Fly.io" guide._
###  Backup and Restore 
To backup/restore your application it is enough to manually copy/replace your `pb_data` directory _(for transactional safety make sure that the application is not running)_.
To make things slightly easier, PocketBase v0.16+ comes with built-in backups and restore APIs that could be accessed from the Dashboard ( _Settings_ > _Backups_ ):
![Backups settings screenshot](https://pocketbase.io/images/screenshots/backups.png)
Backups can be stored locally (default) or in a S3 compatible storage (_it is recommended to use a separate bucket only for the backups_). The generated backup represents a full snapshot as ZIP archive of your `pb_data` directory (including the locally stored uploaded files but excluding any local backups or files uploaded to S3).
During the backup's ZIP generation the application will be temporary set in read-only mode.
Depending on the size of your `pb_data` this could be a very slow operation and it is advised in case of large `pb_data` (e.g. 2GB+) to consider a different backup strategy _(see an examplebackup.sh script that combines `sqlite3 .backup` + `rsync`) _.
###  Recommendations 
By default, PocketBase uses the internal Unix `sendmail` command for sending emails. While it's OK for development, it's not very useful for production, because your emails most likely will get marked as spam or even fail to deliver.
To avoid deliverability issues, consider using a local SMTP server or an external mail service like MailerSend, Brevo, SendGrid, Mailgun, AWS SES, etc.
Once you've decided on a mail service, you could configure the PocketBase SMTP settings from the _Dashboard > Settings > Mail settings _:
![SMTP settings screenshot](https://pocketbase.io/images/screenshots/smtp-settings.png)
As an additional layer of security you can enable the MFA and OTP options for the `_superusers` collection, which will enforce an additional one-time password (email code) requirement when authenticating as superuser.
In case of email deliverability issues, you can also generate an OTP manually using the `./pocketbase superuser otp yoursuperuser@example.com` command.
![Superusers MFA settings screenshot](https://pocketbase.io/images/screenshots/superusers_mfa.png)
To minimize the risk of API abuse (e.g. excessive auth or record create requests) it is recommended to setup a rate limiter.
PocketBase v0.23.0+ comes with a simple builtin rate limiter that should cover most of the cases but you are also free to use any external one via reverse proxy if you need more advanced options.
You can configure the builtin rate limiter from the _Dashboard > Settings > Application:_
![Rate limit settings screenshot](https://pocketbase.io/images/screenshots/rate-limit-settings.png)
The below instructions are for Linux but other operating systems have similar mechanism.
Unix uses _"file descriptors"_ also for network connections and most systems have a default limit of ~ 1024. If your application has a lot of concurrent realtime connections, it is possible that at some point you would get an error such as: `Too many open files`.
One way to mitigate this is to check your current account resource limits by running `ulimit -a` and find the parameter you want to change. For example, if you want to increase the open files limit (_-n_), you could run `ulimit -n 4096` before starting PocketBase.
If you are running in a memory constrained environment, defining the `GOMEMLIMIT` environment variable could help preventing out-of-memory (OOM) termination of your process. It is a "soft limit" meaning that the memory usage could still exceed it in some situations, but it instructs the GC to be more "aggressive" and run more often if needed. For example: `GOMEMLIMIT=512MiB`.
If after `GOMEMLIMIT` you are still experiencing OOM errors, you can try to enable swap partitioning (if not already) or open a Q&A discussion with some steps to reproduce the error in case it is something that we can improve in PocketBase.
It is fine to ignore the below if you are not sure whether you need it.
By default, PocketBase stores the applications settings in the database as plain JSON text, including the SMTP password and S3 storage credentials.
While this is not a security issue on its own (PocketBase applications live entirely on a single server and its expected only authorized users to have access to your server and application data), in some situations it may be a good idea to store the settings encrypted in case someone get their hands on your database file (e.g. from an external stored backup).
To store your PocketBase settings encrypted:
  1. Create a new environment variable and **set a random 32 characters** string as its value. e.g. add `export PB_ENCRYPTION_KEY="XZ07RPCTmBKWqUk2SGKTj5CNyMjEkXDB"` in your shell profile file
  2. Start the application with `--encryptionEnv=YOUR_ENV_VAR` flag. e.g. `pocketbase serve --encryptionEnv=PB_ENCRYPTION_KEY`


