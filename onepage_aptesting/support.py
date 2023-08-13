from functools import lru_cache

import httpx
from activitypub_testsuite.http.client import (
    HttpxLocalActor,
    HttpxServerTestSupport,
    httpx_get_json,
)
from activitypub_testsuite.http.token import HTTPTokenAuth
from activitypub_testsuite.interfaces import Actor


class OnepageServerTestSupport(HttpxServerTestSupport):
    def __init__(self, local_base_url, remote_base_url, request):
        super().__init__(
            local_base_url,
            remote_base_url,
            request,
            # onepage uses a default default media type
            default_media_type="application/activity+json",
        )

    @lru_cache
    def get_local_actor(self, actor_name: str = "local_actor_1") -> Actor:
        return OnepageLocalActor(self, actor_name)


class OnepageLocalActor(HttpxLocalActor):
    def get_profile(self, server, actor_name) -> dict:
        actor_id, token = self._register_user(server, actor_name)
        # this will override the base class init of auth
        self.auth = HTTPTokenAuth(token)
        return httpx_get_json(actor_id, self.auth, "application/activity+json")

    @staticmethod
    def _register_user(server, actor_name):
        register_url = f"{server.local_base_url}/register"
        response = httpx.post(
            register_url,
            data={
                "username": actor_name,
                "password": "PASSWORD",
                "confirmation": "PASSWORD",
            },
            verify=False,
        )
        if response.is_success:
            return (
                response.headers["X-Opp-Actor"],
                response.headers["X-Opp-Token"],
            )
        else:
            print(response)
            raise Exception("User registration failed")
