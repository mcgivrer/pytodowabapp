% rebase('base.tpl', title='Home')
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>my tasks items</h2>
<ul border="1">
%for row in rows:
<li>
    <input type="checkbox" id="{{row[1]}}" value="{{row[3]}}" /><span>{{row[2]}}</span>
</li>
%end
</ul>
