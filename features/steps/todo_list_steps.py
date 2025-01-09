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
    context.manager = TaskManager()  # Ensure TaskManager is initialized
    for row in context.table:
        due_date = row.get('Due Date', None)
        due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
        status = row.get('Status', "Pending")
        task = Task(len(context.manager.tasks) + 1, row['Task'], due_date)
        if status == "Completed":
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
    context.task_list_output = [(task.description, task.due_date.strftime("%Y-%m-%d"), "Completed" if task.completed else "Pending")
                                 for task in context.manager.tasks]


@then('the output should match the displayed tasks')
def step_impl(context):
    expected_output = [(row['Task'], row['Due Date'], row['Status']) for row in context.table]
    assert context.task_list_output == expected_output, "Displayed tasks do not match the expected output."


# Mark a task as completed
@when('the user marks the task "{description}" as completed')
def step_impl(context, description):
    for task in context.manager.tasks:
        if task.description == description:
            task.set_completed()


@then('the statuses of tasks should match')
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


# Update a task
@when('the user updates the task "{description}" with description "{new_description}" and due date "{new_due_date}"')
def step_impl(context, description, new_description, new_due_date):
    for task in context.manager.tasks:
        if task.description == description:
            task.description = new_description
            task.due_date = datetime.strptime(new_due_date, "%Y-%m-%d")


@then('the updated tasks should match the task list')
def step_impl(context):
    expected_tasks = [(row['Task'], row['Due Date']) for row in context.table]
    actual_tasks = [(task.description, task.due_date.strftime("%Y-%m-%d")) for task in context.manager.tasks]
    assert actual_tasks == expected_tasks, "The tasks do not match the expected updates."


# Display pending tasks
@when('the user views the pending tasks')
def step_impl(context):
    context.pending_tasks_output = [(task.description, "Pending") for task in context.manager.tasks if not task.completed]


@then('the pending tasks should match the output')
def step_impl(context):
    expected_pending = [(row['Task'], row['Status']) for row in context.table]
    assert context.pending_tasks_output == expected_pending, "Pending tasks output does not match expected."


# Organize tasks by due date
@when('the user organizes tasks by due date')
def step_impl(context):
    context.manager.organize_tasks_by_date()


@then('the tasks should be sorted by due date')
def step_impl(context):
    sorted_tasks = [(row['Task'], row['Due Date']) for row in context.table]
    actual_tasks = [(task.description, task.due_date.strftime("%Y-%m-%d")) for task in context.manager.tasks]
    assert actual_tasks == sorted_tasks, "The tasks are not sorted as expected."
