
def print_from_stream(n, stream=None):
    if stream is None:
    	stream=Evenstream()
    for _ in range(n):
        print(stream.get_next())

