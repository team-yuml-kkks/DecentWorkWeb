import os
import json

from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

from .exceptions import NoManifestFileException, NoAssetInManifestFile


def get_static_url(resource_path: str, extension: str):
    """Gets static url to resource file.

    Returns:
        Static url to filename.

    Raises:
        NoAssetInManifestFile: When no asset in the manifest file with specific filename.
    """
    data = _read_manifest_file()

    if data:
        filename = data.get(
            '{}.{}'.format(resource_path, extension), None)

        if filename is None:
            raise NoAssetInManifestFile('No ' + filename + ' in manifest file.')

        return static(filename)


def _read_manifest_file():
    """Reads manifest file.

    Returns:
        If no exception returns json data with filenames and their static paths.

    Raises:
        NoManifestFileException: When no manifest file at path in WEBPACK_MANIFEST_FILE setting.
        ValueError: When file does not contain valid json data.
        IOError: When error while reading file.
    """
    path = os.path.normpath(settings.WEBPACK_MANIFEST_FILE['FILE'])

    try:
        with open(path) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        raise NoManifestFileException(
            'No manifest file at this path ' + path + 'check WEBPACK_MANIFEST_FILE setting.'
        )
    except json.JSONDecodeError:
        raise ValueError('Manifest file do not contains valid json data.')
    except IOError:
        raise IOError('Error while reading manifest file.')
