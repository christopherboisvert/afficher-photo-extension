"""voir-ma-photo handler."""

from gateway_addon import APIHandler, APIResponse
import json
import os


class VoirMaPhotoHandler(APIHandler):
    """voir-ma-photo handler."""

    def __init__(self, verbose=False):
        """Initialize the object."""
        manifest_fname = os.path.join(
            os.path.dirname(__file__),
            '..',
            'manifest.json'
        )

        with open(manifest_fname, 'rt') as f:
            manifest = json.load(f)

        APIHandler.__init__(self, manifest['id'])
        self.manager_proxy.add_api_handler(self)

    def handle_request(self, request):
        """
        Handle a new API request for this handler.

        request -- APIRequest object
        """
        if request.method != 'POST' or request.path != '/voir-ma-photo':
            return APIResponse(status=404)

        statut_affichage_photo = {"afficher_photo":true}

        # echo back the body
        return APIResponse(
          status=200,
          content_type='application/json',
          content=json.dumps(statut_affichage_photo),
        )
