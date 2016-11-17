<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/css/normalize.css">
    <link rel="stylesheet" href="/static/css/skeleton.css">
</head>
<body>
    <table>
        <tr>
            <th>LP</th>
            <th>Name</th>
            <th>Material ID</th>
            <th>Company ID</th>
            <th>Material ID</th>
            <th>Description</th>
            <th>Notes</th>
            <th>Supplier</th>
            <th>Price</th>
            <th>Currency</th>
        </tr>
    % for n, i in enumerate(material, start=1):
        <tr>
            <td>{{n}}.</td>
            <td>{{i['name']}}</td>
            <td>{{i['ID']}}</td>
            <td>{{i['id']}}</td>
            <td>{{i['description']}}</td>
            <td>{{i['notes']}}</td>
            <td>{{i['supplier']}}</td>
            <td>{{i['price']}}</td>
            <td>{{i['currency']}}</td>
            <td><a href="/material/{{i['ID']}}/edit/" class="button">edit</a> | <a href="/material/{{i['ID']}}/restore/" class="button">restore</a>  </td>
        </tr>
    % end
    </table>
    <td><a href="http://localhost:8080/companies/">home</a>
</body>