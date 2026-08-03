from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite_console.utils.deprecated import deprecated
from ..enums.block_resource_type import BlockResourceType
from ..enums.block_mode import BlockMode
from ..models.block import Block
from ..models.block_delete import BlockDelete
from ..models.block_list import BlockList
from ..enums.region import Region
from ..enums.cache_target import CacheTarget
from ..enums.cache_database import CacheDatabase
from ..models.user import User

T = TypeVar('T')

class Manager(Service):

    def __init__(self, client) -> None:
        super(Manager, self).__init__(client)

    def create_block(
        self,
        project_id: str,
        resource_type: BlockResourceType,
        resource_id: Optional[str] = None,
        mode: Optional[BlockMode] = None,
        reason: Optional[str] = None,
        expired_at: Optional[str] = None
    ) -> Block:
        """
        Creates a new resource block.

        Parameters
        ----------
        project_id : str
            Project ID
        resource_type : BlockResourceType
            Resource type to block (e.g., projects, functions, databases, storage, etc.)
        resource_id : Optional[str]
            Optional resource ID (if omitted, all resources of this type will be blocked)
        mode : Optional[BlockMode]
            Block mode. Use full to block reads and writes, or readOnly to block database writes only.
        reason : Optional[str]
            Optional reason why the resource is blocked
        expired_at : Optional[str]
            Optional expiration date for the block
        
        Returns
        -------
        Block
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/manager/blocks'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')


        api_params['projectId'] = self._normalize_value(project_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)
        if mode is not None:
            api_params['mode'] = self._normalize_value(mode)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)
        if expired_at is not None:
            api_params['expiredAt'] = self._normalize_value(expired_at)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Block)


    def delete_block(
        self,
        project_id: str,
        resource_type: BlockResourceType,
        resource_id: Optional[str] = None
    ) -> BlockDelete:
        """
        Deletes resource blocks for a project.

        Parameters
        ----------
        project_id : str
            Project ID
        resource_type : BlockResourceType
            Resource type to unblock
        resource_id : Optional[str]
            Optional resource ID (if omitted, all blocks of this type will be removed)
        
        Returns
        -------
        BlockDelete
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/manager/blocks'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        if resource_type is None:
            raise AppwriteException('Missing required parameter: "resource_type"')


        api_params['projectId'] = self._normalize_value(project_id)
        api_params['resourceType'] = self._normalize_value(resource_type)
        if resource_id is not None:
            api_params['resourceId'] = self._normalize_value(resource_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BlockDelete)


    def list_blocks(
        self,
        project_id: str
    ) -> BlockList:
        """
        Lists all resource blocks for a project.

        Parameters
        ----------
        project_id : str
            Project ID
        
        Returns
        -------
        BlockList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/manager/blocks/{projectId}'
        api_params = {}
        if project_id is None:
            raise AppwriteException('Missing required parameter: "project_id"')

        api_path = api_path.replace('{projectId}', str(self._normalize_value(project_id)))


        response = self.client.call('get', api_path, {
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=BlockList)


    def delete_cache(
        self,
        region: Optional[Region] = None,
        cache: Optional[CacheTarget] = None,
        all: Optional[bool] = None,
        database: Optional[CacheDatabase] = None,
        project_id: Optional[str] = None,
        collection_id: Optional[str] = None,
        document_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Clears internal cache.

        Parameters
        ----------
        region : Optional[Region]
            Target region.
        cache : Optional[CacheTarget]
            Cache target.
        all : Optional[bool]
            Clear the entire selected cache target.
        database : Optional[CacheDatabase]
            Database cache scope.
        project_id : Optional[str]
            Project ID for project or logs database cache.
        collection_id : Optional[str]
            Collection ID.
        document_id : Optional[str]
            Document ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/manager/cache'
        api_params = {}

        if region is not None:
            api_params['region'] = self._normalize_value(region)
        if cache is not None:
            api_params['cache'] = self._normalize_value(cache)
        if all is not None:
            api_params['all'] = self._normalize_value(all)
        if database is not None:
            api_params['database'] = self._normalize_value(database)
        if project_id is not None:
            api_params['projectId'] = self._normalize_value(project_id)
        if collection_id is not None:
            api_params['collectionId'] = self._normalize_value(collection_id)
        if document_id is not None:
            api_params['documentId'] = self._normalize_value(document_id)

        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return response


    def update_user_status(
        self,
        status: bool,
        user_id: Optional[str] = None,
        email: Optional[str] = None,
        reason: Optional[str] = None,
        model_type: Type[T] = dict
    ) -> User[T]:
        """
        Updates a console user status using a user ID or email address.

        Parameters
        ----------
        status : bool
            User status. Set to `false` to block and `true` to unblock.
        user_id : Optional[str]
            User ID.
        email : Optional[str]
            User email address.
        reason : Optional[str]
            Optional reason when blocking a user. Accepted for parity with the CLI task but not persisted.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        User[T]
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/manager/users/status'
        api_params = {}
        if status is None:
            raise AppwriteException('Missing required parameter: "status"')


        if user_id is not None:
            api_params['userId'] = self._normalize_value(user_id)
        if email is not None:
            api_params['email'] = self._normalize_value(email)
        api_params['status'] = self._normalize_value(status)
        if reason is not None:
            api_params['reason'] = self._normalize_value(reason)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return User.with_data(response, model_type)

