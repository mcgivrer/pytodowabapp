% rebase('templates/base.tpl', title='Add new task')
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="POST">
	<select name="priority" >
		<option value="0">Low</option>
		<option value="1">Medium</option>
		<option value="2">High</option>
	</select>
  <input type="text" size="400" maxlength="400" name="description">
  <input type="submit" name="save" value="save">
</form>