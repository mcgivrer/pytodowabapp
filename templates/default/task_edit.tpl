% rebase('templates/base.tpl', title='Edit a task')
<div class="form">
	<p>Edit a task</p>
	<form action="/task" method="POST">
		<input type="hidden" name="id" value="{{old['id']}}"/>
		<dl>
			<dt>ToDo list ID</dt>
			<dd><input type="text" name="todoId" value="{{old['todoId']}}"/></dd>
			<dt>Author</dt>
			<dd><input type="text" name="username" value="{{old['author']}}"/></dd>
			<dt>Priority</dt>
			<dd>
				<select name="priority" value="{{old['priority']}}">
					<option value="0">Low</option>
					<option value="1">Medium</option>
					<option value="2">High</option>
				</select>
			</dd>
			<dt>Description</dt>
			<dd>
				<textarea size="80" maxlength="400" cols="80" rows="5" name="description">{{old['description']}}</textarea>
			</dd>
			<dt>Status</dt>
			<dd>
			<select name="status" value="{{old['status']}}">
				<option value="0">ToDo</option>
				<option value="1">Done</option>
			</select>
			</dd>
		</dl>
		<input type="submit" name="save" value="Save" accesskey="S" title="Save the modified Task">
		<a class="button" href="/tasks" title="Back to Task list" accesskey="C">Cancel</a>
	</form>
</div>
