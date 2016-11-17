<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <div class="container">
        <form action="/login/" method="POST">
            <div class="row">
                username: <input name="username" type="text" />
            </div>
            <div class="row">
                password: <input name="password" type="password" />
            </div>
            <input value="Login" type="submit" />
        </form>
    </div>
</body>