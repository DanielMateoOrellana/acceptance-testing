from behave import given, when, then
from main import TaskManager, Task
from datetime import datetime

# Initialize the task manager for all scenarios
@given('the task list is empty')
def step_impl(context):
    context.manager = TaskManager()
    context.manager.remove_all_tasks()

# Populate the task list
@given('the task list contains tasks')
def step_impl(context):
    context.manager = TaskManager()
    for row in context.table:
        due_date = datetime.strptime(row['Due Date'], "%Y-%m-%d")
        task = Task(len(context.manager.tasks) + 1, row['Task'], due_date)
        if 'Status' in row and row['Status'] == "Completed":
            task.set_completed()
        context.manager.create_task(task)

# Create a new task
@when('the user creates a task "{description}" with due date "{due_date}"')
def step_impl(context, description, due_date):
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    task = Task(len(context.manager.tasks) + 1, description, due_date)
    context.manager.create_task(task)

@then('the task list should contain "{description}"')
def step_impl(context, description):
    tasks = [task.description for task in context.manager.tasks]
    assert description in tasks, f'Task "{description}" not found in the task list.'

# View all tasks
@when('the user views the task list')
def step_impl(context):
    context.task_list_output = [
        (task.description, task.due_date.strftime("%Y-%m-%d"), "Completed" if task.completed else "Pending")
        for task in context.manager.tasks
    ]

@then('the output should show')
def step_impl(context):
    expected_output = [(row['Task'], row['Due Date'], row['Status']) for row in context.table]
    assert context.task_list_output == expected_output, "Displayed tasks do not match the expected output."

# Mark a task as completed
@when('the user marks the task "{description}" as completed')
def step_impl(context, description):
    for task in context.manager.tasks:
        if task.description == description:
            task.set_completed()

@then('the task list should show')
def step_impl(context):
    expected_status = {row['Task']: row['Status'] for row in context.table}
    for task in context.manager.tasks:
        actual_status = "Completed" if task.completed else "Pending"
        assert actual_status == expected_status[task.description], f'Status for task "{task.description}" does not match expected.'

# Remove all tasks
@when('the user clears all tasks')
def step_impl(context):
    context.manager.remove_all_tasks()

@then('the task list should be empty')
def step_impl(context):
    assert len(context.manager.tasks) == 0, "The task list is not empty."

# Add multiple tasks (new scenario step)
@when('the user creates multiple tasks')
def step_impl(context):
    for row in context.table:
        due_date = datetime.strptime(row['Due Date'], "%Y-%m-%d")
        task = Task(len(context.manager.tasks) + 1, row['Task'], due_date)
        context.manager.create_task(task)

@then('the task list should contain the following tasks')
def step_impl(context):
    expected_tasks = [(row['Task'], row['Due Date']) for row in context.table]
    actual_tasks = [(task.description, task.due_date.strftime("%Y-%m-%d")) for task in context.manager.tasks]
    assert actual_tasks == expected_tasks, "The tasks in the list do not match the expected tasks."

# Verify no tasks exist (new scenario step)
@then('the task list should be empty (verification)')
def step_impl(context):
    assert len(context.manager.tasks) == 0, "The task list is not empty."
