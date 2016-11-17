<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <form action="/companies/" method="POST">
    <table>
        <tr>
            <th>LP</th>
            <th>Name</th>
            <th></th>
        </tr>
    % for n, i in enumerate(companies, start=1):
        <tr>
            <td>{{n}}.</td>
            <td>{{i['companyName']}}</td>
            <td><a href="/companies/{{i['companyID']}}/">enter</a></td>
        </tr>
    % end
    </table>
</body>