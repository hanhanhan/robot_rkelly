# R Kelly Song Generator

Have Robot R Kelly write you a song. 

Inspired by:

-[This robotics engineer](https://www.youtube.com/watch?v=20EfiLHG9aY)

-[Daniel Schiffman's explanation of Markov chains](https://www.youtube.com/watch?v=eGFJ8vugIWA)

Things I'd like to change/fix/understand, roughly in order of my own confusedness.
1. When calling the song-lyrics route (is that the right wording?), a title gets randomly generated. About 1 in 6 times, the title value is 'None'. 
I stuck some print statements in for debugging.

[in make_title](https://github.com/hanhanhan/robot_rkelly/blob/master/app/main/views.py#L64):

'''
make_title() telling title_word ['body', 's', 'telling'] title_list Body S Telling title <class 'str'>
'''

[Before the database commit](https://github.com/hanhanhan/robot_rkelly/blob/master/app/main/views.py#L79):

'''
None Title <class 'NoneType'>
127.0.0.1 - - [23/Feb/2017 14:02:59] "GET /song-lyrics/ HTTP/1.1" 302 -
[N]
'''

No suprise after `db.commit()`:
```
linked_lyrics route song title:  None
'''

1. Is there a more conventional spot for the programming?
1. I tried caching the text as a json, and ran `timeit` on loading the file + re-creating the Markov model vs loading the Markov model as a json. (I might not be doing this right.)[https://github.com/hanhanhan/robot_rkelly/blob/master/timeit_test.py]. Is there another place to keep it in scope for re-use? Better caching w/pickle? Recommended to use timeit with something that complex?
2. For a facebook preview image, do I make a (route to the image?)[https://developers.facebook.com/docs/sharing/webmasters]
3. There's a subset of words I can start with - I'm interested in pulling that set out and choosing randomly + re-using to give songs a theme, but not sure how to break into markovify library.
4. What's happening to lowercase everthing in the sentences?
3. I'd love to use a (glitch effect)[https://css-tricks.com/glitch-effect-text-images-svg/] but can't get the words to stack on top of each other properly (CSS)
3. I'd like to make the side bar 'sticky' and have size vary with screen. Use image sets? VW? 
4. I was running into trouble setting this up on PythonAnywhere. Renamed 'app' to 'application'. Need some changes for MySQL
5. Way better practices for config file than putting on github :P
6. Nginx for serving static resources.
7. Webpack or gulp or something to minify, practice using with simple project/low stakes.


