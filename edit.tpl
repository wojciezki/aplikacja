<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <form action="/material/{{id}}/edit/" method="POST">
        {{ !form.mat_name.label }}
        {{ !form.mat_name }}
        {{ !form.comp_id.label }}
        {{ !form.comp_id }}
        {{ !form.description.label }}
        {{ !form.description }}
        {{ !form.notes.label }}
        {{ !form.notes }}
        {{ !form.supplier.label }}
        {{ !form.supplier }}
        {{ !form.price.label }}
        {{ !form.price }}
        {{ !form.currency.label }}
        {{ !form.currency }}
        <div class="row">
            <input type="submit" value="Wyślij" />
        </div>
    </form>
</body>