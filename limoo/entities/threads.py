class Threads:

    def __init__(self, driver):
        self._driver = driver

    _GET_THREAD_MSG = 'workspace/items/{}/thread/items/{}'
    async def getThreadMessages(self, workspace_id, message_id):
        if workspace_id is None:
            raise "Workspace_id is needed"
        return await self._driver._execute_api_get(self._GET_THREAD_MSG.format(workspace_id, message_id))

    _FOLLOW_THREAD = 'workspace/items/{}/thread/items/{}/follow'
    async def follow(self, workspace_id, message_id):
        if workspace_id is None:
            raise "Workspace_id is needed"
        return await self._driver._execute_api_post(self._FOLLOW_THREAD.format(workspace_id, message_id), body = [])

    _UNFOLLOW_THREAD = 'workspace/items/{}/thread/items/{}/unfollow'
    async def unfollow(self, workspace_id, message_id):
        if workspace_id is None:
            raise "Workspace_id is needed"
        return await self._driver._execute_api_post(self._UNFOLLOW_THREAD.format(workspace_id, message_id), body = [])
