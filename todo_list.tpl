% rebase('base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>my tasks items</h2>
<ul border="1">
%for row in rows:
<li>
    <input type="checkbox" id="{{row["id"]}}" value="{{row["status"]}}" /><span>{{row["task"]}}</span>
</li>
%end
</ul>
