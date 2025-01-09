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

  Scenario: Update a task
    Given the task list contains tasks
      | Task          | Due Date   |
      | Buy groceries | 2025-01-15 |
    When the user updates the task "Buy groceries" with description "Buy milk" and due date "2025-01-18"
    Then the task list should show
      | Task     | Due Date   |
      | Buy milk | 2025-01-18 |

  Scenario: Display pending tasks
    Given the task list contains tasks
      | Task          | Due Date   | Status    |
      | Buy groceries | 2025-01-15 | Completed |
      | Pay bills     | 2025-01-20 | Pending   |
    When the user views the pending tasks
    Then the output should show
      | Task      | Status  |
      | Pay bills | Pending |

  Scenario: Organize tasks by due date
    Given the task list contains tasks
      | Task          | Due Date   |
      | Pay bills     | 2025-01-20 |
      | Buy groceries | 2025-01-15 |
    When the user organizes tasks by due date
    Then the task list should show
      | Task          | Due Date   |
      | Buy groceries | 2025-01-15 |
      | Pay bills     | 2025-01-20 |
