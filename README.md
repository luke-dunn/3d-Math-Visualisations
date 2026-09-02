I have tried to make a kind of pipeline where different geometric shapes, from random walks to Hilbert curves and more, are animated simply and cleanly for 3d viewing. I've used Python3.12.

`animate.py` and `transform.py` are designed to be more or less immutable. Each shape has a generator function that lives in `shapes.py`. The functions in `shapes.py` are designed to return a list consisting of pairwise tuples. each tuple is simply the start and end point of a line, nothing else' The list of lines is passed to the other components to be drawn.

The animate script creates an mp4 video composed of png frames then adds a synth soundtrack that depends algorithmically on each frame's pixel structure. 

`transform3d.py` provides a rotating viewpoint to allow the structure of these wonderful 3d shapes to be seen more clearly.

Example shown is `hyperboloid.py` which can be run with the other files present in the current directory to see the concept.

Requires `ffmpeg` too. 

The result is simple and fairly lo-fi, perhaps suitable for playing with and extending as a beginner project. I stayed low level using hard coded Python, rather than a more high level approach such as Mathematica which could probably render all these as one-liners! But the point was to learn the mechanics myself, not just to abstract most of the code away and let someone else do the hard bits.

It's really on the level of something that would have been seen as 'advanced' in around the mid 70s, but it has been fun for yours truly.
