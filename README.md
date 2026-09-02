I have tried to make a kind of pipeline where different geometric shapes, from random walks to Hilbert curves and more, are animated simply and cleanly for 3d viewing. I've used Python3.12.

`animate.py` and `transform.py` are designed to be more or less immutable. Each shape has a generator function that lives in `shapes.py`.

The animate script creates an mp4 video composed of png frames then adds a synth soundtrack that depends algorithmically on each frame's pixel structure.

Example shown is `hyperboloid.py` which can be run with the other files present in the current directory to see the concept.

