% rebase('templates/base.tpl', title='Edit a task')
<p>Add a new task to the ToDo list:</p>
<form action="/task" method="POST">
  <input type="hidden" name="id" value="{{old['id']}}"/>
	<select name="priority" value="{{old['priority']}}">
		<option value="0">Low</option>
		<option value="1">Medium</option>
		<option value="2">High</option>
	</select>
  <input type="text" size="400" maxlength="400" name="description" value="{{old['priority']}}">
  <input type="text" size="400" maxlength="400" name="description" value="{{old['description']}}">
  <input type="hidden" name="status" value="{{old['status']}}"/>
  <input type="submit" name="save" value="save">
</form>
