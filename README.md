# R Kelly Song Generator

Have Robot R Kelly write you a song. 

Inspired by:

-[This robotics engineer](https://www.youtube.com/watch?v=20EfiLHG9aY)

-[Daniel Schiffman's explanation of Markov chains](https://www.youtube.com/watch?v=eGFJ8vugIWA)

Things I'd like to change/fix/understand:


1. I tried caching the model as a json, and ran `timeit` on loading the file + re-creating the Markov model vs loading the Markov model as a json. [I might not be doing this right.](https://github.com/hanhanhan/robot_rkelly/blob/master/timeit_test.py). Is there another place to keep it in scope for re-use? Better caching w/pickle? Recommended to use timeit with something that complex?
1. Is there a more conventional/better spot for programming making the individual song?
2. For a facebook preview image, do I make a (route to the image?)[https://developers.facebook.com/docs/sharing/webmasters]
3. There's a subset of words I can start with - I'm interested in pulling that set out and choosing randomly + re-using to give songs a theme, but not sure how to break into markovify library.
4. What's happening to lowercase everthing in the sentences?
3. I'd love to use a [glitch effect](https://css-tricks.com/glitch-effect-text-images-svg/) but can't get the words to stack on top of each other properly (CSS)
3. I'd like to make the side bar 'sticky' and have size vary with screen. Use image sets? VW? 
4. I was running into trouble setting this up on PythonAnywhere. Renamed 'app' to 'application'. Need some changes for MySQL
5. Way better practices for config file than putting on github :P
6. Nginx for serving static resources.
7. Webpack or gulp or something to minify, practice using with simple project/low stakes.


