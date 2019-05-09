def pytest_configure():
    from addok import hooks
    import addok_http_falcon
    hooks.register(addok_http_falcon)
