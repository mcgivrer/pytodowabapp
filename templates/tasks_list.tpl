% rebase('templates/base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>my tasks items</h2>
<div class="info">{{msg}}</div>
<table class="tasks" border="0">
	<thead><th>#</th><th>task</th><th>priority</th><th>status</th><th colspan="2">actions</th></thead>
    <tbody>
%for row in rows:
<tr class="status{{row['status']}}">
    <td class="id">{{row['id']}}</td>
    <td><span>{{row['description']}}</span></td>
    <td class="prio level{{row['priority']}}">{{row['priority']}}</td>
    %if row['status']==0:
    <td class="action"><a href="/done/{{row['id']}}">TODO</td>
    %end
    %if row['status']==1:
    <td class="action"><a href="/todo/{{row['id']}}">DONE</td>
    %end
    <td class="action"><a href="/task/{{row['id']}}">edit</a></td>
    <td class="action"><a href="/delete/{{row['id']}}">delete</a></td>
</tr>
%end
</tbody>
<tfoot>
    <tr><td colspan="6">&nbsp;</td></tr>
</tfoot>
</table>

<div class="actions"><a href="/new" title="create a new task">create</a>&nbsp;<a href="/delete_all" title="delete">delete</a></div>
