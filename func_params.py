def spam(foo, bar, *blah, baz, biff, **blat):
    print(foo, bar, blah, baz, biff, blat)

spam(5, 10, baz=1, biff=2)
spam(bar=10, foo=5, biff=9, baz="abc")
spam(5, 10, 8, "wombat", "broccoli", baz=99, biff="spaceman", 
     animal="wombat", city="Houston")

def find_text(search_string, *files, ignore_case=False):
    print(f"looking for {search_string} in {files}")

find_text("rabbit", "file1.txt", "f2.txt", 'jackalope.txt', ignore_case=True)