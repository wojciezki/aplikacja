<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <form action="/material/{{id}}/restore/" method="POST">
        <div class="row">
            <div>Are you Sure?</div>
        </div>
        <div class="row">
            <input type="submit" value="ok" />
            <a href="/material/{{id}}/" class="button"> no </a>
        </div>
    </form>
</body>