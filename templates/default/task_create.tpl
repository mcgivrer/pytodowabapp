% rebase('templates/base.tpl', title='Add new task')
<div class="form">
<h2>Add a new task</h2>
<form action="/new" method="POST">
	<dl>
		<dt>ToDo list ID</dt>
		<dd><input type="text" name="todoId" value="1"/></dd>
		<dt>author</dt>
		<dd><input type="text" name="username" value="212391884"/></dd>
		<dt>Priority</dt>
		<dd>
			<select name="priority">
				<option value="0">Low</option>
				<option value="1">Medium</option>
				<option value="2">High</option>
			</select>
		</dd>
		<dt>Description</dt>
		<dd>
			<textarea size="80" maxlength="400" cols="80" rows="5" name="description"></textarea>
		</dd>
	</dl>
  <input type="submit" name="save" value="save">
<a class="button" href="/tasks" title="Back to Task list" accesskey="C">Cancel</a>
</form>
</div>