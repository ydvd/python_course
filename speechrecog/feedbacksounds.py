import pyglet

# Tutorial goes over using pyaudio as he couldn't get pyglet to work 
# but turns out pyglet is pretty easy so there we go
file = pyglet.resource.media('audio/start.mp3')

file.play()

pyglet.app.run()