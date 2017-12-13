% rebase('templates/base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>my tasks items</h2>
<div class="info">{{msg}}</div>
<table border="0">
	<thead><th>priority</th><th>task</th><th>status</th><th colspan="2">actions</th></thead>
%for row in rows:
<tr>
    <td>{{row['priority']}}</td>
    <td><span>{{row['description']}}</span></td>
    %if row['status']==0:
    <td><a href="/done/{{row['id']}}">TODO</td>
    %end
    %if row['status']==1:
    <td><a href="/todo/{{row['id']}}">DONE</td>
    %end
    <td><a href="/task/{{row['id']}}">edit</a></td><td><a href="/delete/{{row['id']}}">delete</a></td>
</tr>
%end
</table>

<div><a href="/new" title="create a new task">create</a>&nbsp;<a href="/delete_all" title="delete">delete</a></div>
