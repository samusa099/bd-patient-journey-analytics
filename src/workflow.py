VALID=['ordered','ready','accepted','in_progress','completed','cancelled','exception']
def transition(task,state):
    if state not in VALID: raise ValueError('invalid state')
    task=dict(task);task['task_status']=state;return task
