import pyglet

file = pyglet.resource.media('audio/start.mp3')

file.play()

pyglet.app.run()