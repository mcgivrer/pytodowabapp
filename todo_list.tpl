% rebase('base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h1>Here is your ToDo list</h1>
<p>The open items are as follows:</p>
<ul border="1">
%for row in rows:
<li>
    <input type="checkbox" id="{{row[1]}}" value="{{row[3]}}" /><span>{{row[2]}}</span>
</li>
%end
</ul>
