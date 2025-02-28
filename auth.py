from gql.transport.aiohttp import AIOHTTPTransport

def get_cookie() -> str:
    return ''

def get_token() -> str:
    return ''

def get_headers() -> dict[str, str]:
    return {
        "Cookie": get_cookie(),
        "X-Csrftoken": get_token(),
    }

def get_transport() -> AIOHTTPTransport:
    return AIOHTTPTransport(url="https://leetcode.com/graphql", headers=get_headers())