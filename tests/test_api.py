from playwright.sync_api import sync_playwright

def test_get_users_api():

    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
        print(data)
        assert response.status == 200
        assert len(data) > 0
        assert data[0]["name"] == "Leanne Graham"