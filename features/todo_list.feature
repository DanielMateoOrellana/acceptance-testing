Feature: Task Management System
  As a user, I want to manage my tasks efficiently so that I can stay organized.

  Scenario: Create a new task
    Given the task list is empty
    When the user creates a task "Buy groceries" with due date "2025-01-15"
    Then the task list should contain "Buy groceries"

  Scenario: Display all tasks
    Given the task list contains tasks
      | Task          | Due Date   | Status  |
      | Buy groceries | 2025-01-15 | Pending |
      | Pay bills     | 2025-01-20 | Pending |
    When the user views the task list
    Then the output should show
      | Task          | Due Date   | Status  |
      | Buy groceries | 2025-01-15 | Pending |
      | Pay bills     | 2025-01-20 | Pending |

  Scenario: Mark a task as completed
    Given the task list contains tasks
      | Task          | Due Date   | Status  |
      | Buy groceries | 2025-01-15 | Pending |
    When the user marks the task "Buy groceries" as completed
    Then the task list should show
      | Task          | Status    |
      | Buy groceries | Completed |

  Scenario: Remove all tasks
    Given the task list contains tasks
      | Task          | Due Date   | Status  |
      | Buy groceries | 2025-01-15 | Pending |
      | Pay bills     | 2025-01-20 | Pending |
    When the user clears all tasks
    Then the task list should be empty

  Scenario: Add multiple tasks
    Given the task list is empty
    When the user creates a task "Task 1" with due date "2025-01-10"
    And the user creates a task "Task 2" with due date "2025-01-15"
    Then the task list should contain "Task 1"
    And the task list should contain "Task 2"

  Scenario: Verify no tasks exist
    Given the task list is empty
    Then the task list should be empty
