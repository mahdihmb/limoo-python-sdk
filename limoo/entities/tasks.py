class Tasks:

    def __init__(self, driver):
        self._driver = driver

    _GET_MY_TASKS = 'workspace/items/{}/task/items?per_page=-1'
    async def getMyTasks(self, workspace_id):
        if workspace_id is None:
            raise "Workspace_id is needed for getting tasks"
        return await self._driver._execute_api_get(self._GET_MY_TASKS.format(workspace_id))
