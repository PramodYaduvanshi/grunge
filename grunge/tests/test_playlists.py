from uuid import UUID
from unittest import skip

from furl import furl
from rest_framework import status
from rest_framework.reverse import reverse as drf_reverse

from . import BaseAPITestCase


class PlaylistTests(BaseAPITestCase):
    def setUp(self):
        self.playlist_name = "Faviourite Tracks"
        self.playlist_uuid = UUID("b3083319-47a9-40ed-a4e0-a79d050d9df7")
        self.track_uuid = UUID("b3083319-47a9-40ed-a4e0-a79d050d9df7")

    @skip
    def test_list_playlists(self):
        # Should be able to fetch the list of playlists.
        url = drf_reverse("playlist-list", kwargs={"version": self.version})
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data["count"], 1)    
        #raise NotImplementedError("This test case needs to be implemented.")

    @skip
    def test_search_playlists(self):
        # Should be able to search for playlists by `name`.
        url = drf_reverse("playlist-list", kwargs={"version": self.version})
        url = furl(url).set({"name": self.playlist_name}).url
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data["count"], 3)
        self.assertEqual(r.data["results"][0]["uuid"], self.playlist_uuid)
        self.assertEqual(r.data["results"][0]["tracks"]["uuid"], self.track_uuid)
        

    @skip
    def test_get_playlist(self):
        # Should be able to fetch a playlist by its `uuid`.
        url = drf_reverse(
            'playlist-detail', kwargs={'version': self.version, 'uuid': self.playlist_uuid}
        )
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(
            r.data["name"], self.playlist_name  
        )
        self.assertEqual(
            r.data["tracks"]["uuid"], self.track_uuid
        )

    @skip
    def test_create_playlist(self):
        # Should be able to create a playlist with 0 or more tracks.
        raise NotImplementedError("This test case needs to be implemented.")

    @skip
    def test_update_playlist(self):
        # Should be able to change a playlist's `name`, and add, remove,
        # or re-order tracks.
        raise NotImplementedError("This test case needs to be implemented.")

    @skip
    def test_delete_playlist(self):
        # Should be able to delete a playlist by `uuid`.
        raise NotImplementedError("This test case needs to be implemented.")
