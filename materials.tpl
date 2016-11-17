<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <form action="/companies/{{id}}/" method="POST">
    <table>
        <tr>
            <th>LP</th>
            <th>Name</th>
        </tr>
    % for n, i in enumerate(comp_materials, start=1):
        <tr>
            <td>{{n}}.</td>
            <td>{{i['name']}}</td>
            <td><a href="/material/{{i['ID']}}/">enter</a></td>
        </tr>
    % end
    </table>
    <td><a href="http://localhost:8080/companies/">home</a>
</body>