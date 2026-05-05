# https://developers.google.com/drive/api/guides/manage-uploads
# https://developers.google.com/drive/api/guides/ref-export-formats

__version__ = "dev"

import io

from typing import Optional

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import Resource, build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload


class DriveTool:
    """A tool to interact with the Google Drive API

    Attributes:
        __service (Resource): Google Drive API service
        __creds (Credentials): Credentials of the service account
        
                
    Methods:
        setup(service_account_file: str) -> None
        _authenticate(service_account_file: str) -> Credentials
        upload_file(file_name: str, folder_id: str, mimetype: str) -> str
        export_file(file_id: str, mimetype: str) -> bytes
        download_byte_file(file_id: str, mimetype: str) -> bytes
    """

    def __init__(self):
        self.__service: Optional[Resource] = None
        self.__creds: Optional[Credentials] = None

    def setup(self, service_account_file) -> None:
        """Setup the Google Sheets API

        Args:
            service_account_file (str): Path to the service account file
        """

        try:
            self._authenticate(service_account_file)
            self.__service: Resource = build("drive", "v3", credentials=self.__creds)
        except HttpError as e:
            raise e

    def _authenticate(self, service_account_file: str) -> Credentials:
        """Authenticate the Google Sheets API

        Args:
            service_account_file (str): Path to the service account file

        Returns:
            Credentials: Credentials of the service account
        """

        g_scopes: list = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        try:
            self.__creds = Credentials.from_service_account_file(
                service_account_file, scopes=g_scopes
            )
        except HttpError as e:
            raise e
        
    def upload_file(self, file_name: str, folder_id: str, mimetype: str) -> str:
        """Upload a file to Google Drive.
        
        Args:
            file_name (str): Name of the file to upload
            folder_id (str): ID of the folder to upload the file to
            mimetype (str): Mimetype of the file to upload

        Returns:
            str: ID of the uploaded file

        Possible mimetypes:
            https://developers.google.com/drive/api/v3/mime-types
        """

        file_metadata = {
            "name": file_name,
            "parents": [folder_id]
        }
        media = MediaFileUpload(file_name, mimetype=mimetype)
        file = self.__service.files().create(body=file_metadata, media_body=media, fields="id").execute()

        return file.get("id")
    
    def export_file(self, file_id: str, mimetype: str) -> bytes:
        """Export a file from Google Drive.

        Args:
            file_id (str): ID of the file to export
            mimetype (str): Mimetype of the file to export

        Returns:
            bytes: The exported file
        
        Possible mimetypes:
            https://developers.google.com/drive/api/v3/ref-export-formats
        """

        request = self.__service.files().export_media(fileId=file_id, mimeType=mimetype)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        return file
    
    def download_byte_file(self, file_id: str, mimetype: str):
        """Download a file from Google Drive.

        Args:
            file_id (str): ID of the file to download
            mimetype (str): Mimetype of the file to download

        Returns:
            bytes: The downloaded file

        Possible mimetypes:
            https://developers.google.com/drive/api/v3/mime-types
        """

        file_id = file_id

        request = self.__service.files().get_media(fileId=file_id, mimeType=mimetype)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        return file