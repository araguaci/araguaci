One-Line Web Server 🖥️
==================================================================================


The following commands will each start a simple web server, serving up the files in the current directory.  
Just open up the browser, and navigate to the system's IP + port (e.g. `http://localhost:8080`).

### Python

```
python -m http.server 8000

```
    

* * *

### Node.js

```
npx http-server ./ --port 8080

```
    

* * *

### PHP

```
php -S 127.0.0.1:8080

```

    

* * *

### Ruby

```
ruby -run -e httpd ./ -p 8080

```
    

* * *

### R

```
Rscript -e 'servr::httd()' -p8080

```
    

* * *

### Caddy

[Caddy](https://caddyserver.com/) is a feature-rich production-ready Go-based web server, with easy configuration. Just download and use something like the following command.

```
caddy file-server

```
    

* * *

### Rust (with [miniserve](https://github.com/svenstaro/miniserve))

```
cargo install miniserve
miniserve -p 8080 .
```
    

* * *

### BusyBox

```
busybox httpd -f -p 8080

```
    

* * *

You can also share the server with someone remotely,  
see: [Using Ngrok to expose server to the internet](https://notes.aliciasykes.com/p/RUi22QSyWe)
