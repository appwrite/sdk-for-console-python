from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite_console.utils.deprecated import deprecated

class Assistant(Service):

    def __init__(self, client) -> None:
        super(Assistant, self).__init__(client)

    def chat(
        self,
        prompt: str
    ) -> Dict[str, Any]:
        """
        Send a prompt to the AI assistant and receive a response. This endpoint allows you to interact with Appwrite's AI assistant by sending questions or prompts and receiving helpful responses in real-time through a server-sent events stream. 

        Parameters
        ----------
        prompt : str
            Prompt. A string containing questions asked to the AI assistant.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/console/assistant'
        api_params = {}
        if prompt is None:
            raise AppwriteException('Missing required parameter: "prompt"')


        api_params['prompt'] = self._normalize_value(prompt)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'text/plain',
        }, api_params)

        return response

