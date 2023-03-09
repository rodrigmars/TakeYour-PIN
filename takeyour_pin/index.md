# Api REST TakeYour-PIN

Application developed in Bottle a WSGI micro web-framework.

```rest
GET http:localhost/pin/<your_email>
```

```python

    app = Bottle()

    @app.route('/')
    def home():
        return {}

```
