% rebase('templates/base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>{{todo['name']}}</h2>
<div class="message info"><p>{{message}}</p></div>
%if len(tasks) > 0:
<table class="tasks" border="0">
	<thead><th>#</th><th>Actor</th><th>Description</th><th>Priority</th><th>Status</th><th colspan="2">Actions</th></thead>
    <tbody>
%for task in tasks:
<tr class="status{{task['status']}}">
    <td class="id">{{task['id']}}</td>
    <td><span><a href="mailto:{{task['useremail']}}">({{task['username']}}) {{task['firstname']}} {{task['lastname']}}</a></span></td>
    <td><span>{{task['description']}}</span></td>
    <td class="prio level{{task['priority']}}">{{task['priority']}}</td>
    %if task['status']==0:
    <td class="action"><a href="/done/{{task['id']}}">TODO</td>
    %end
    %if task['status']==1:
    <td class="action"><a href="/todo/{{task['id']}}">DONE</td>
    %end
    %if task['status']==2:
    <td class="action"><a href="/done/{{task['id']}}">UNARCHIVE</td>
    %end
    <td class="action"><a href="/task/{{task['id']}}">edit</a></td>
    <td class="action"><a href="/archive/{{task['id']}}">archive</a></td>
</tr>
%end
</tbody>
<tfoot>
    <tr><td colspan="6">&nbsp;</td></tr>
</tfoot>
</table>
%else:
<p>There no tasks.</p>
%end
<div class="actions" style="float:left;">
    <a href="/tasks" title="Show archived tasks" accesskey="t">[T]asks</a>
    <a href="/archives" title="Show archived tasks" accesskey="a">Show [A]rchives</a>
</div>
<div class="actions">
    <a href="/new" title="Create a new task" accesskey="c">[C]reate</a>&nbsp;
</div>
