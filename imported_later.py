def bar():
    print("in imported_later.bar")
    with open("/tmp/z", "w") as f:
        f.write("hello world")
