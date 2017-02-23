# R Kelly Song Generator

Have Robot R Kelly write you a song. 

Inspired by:
*[This robotics engineer](https://www.youtube.com/watch?v=20EfiLHG9aY)
*[Daniel Schiffman's explanation of Markov chains](https://www.youtube.com/watch?v=eGFJ8vugIWA)

Things I'd like to change/fix/understand, roughly in order of my own confusedness.
1. When calling the song-lyrics route (is that the right wording?), a title gets randomly generated. About 1 in 6 times, the title value is 'None'. 
I stuck some print statements in for debugging.

[in make_title](https://github.com/hanhanhan/robot_rkelly/blob/master/app/main/views.py#L64):
'''
make_title() telling title_word ['body', 's', 'telling'] title_list Body S Telling title <class 'str'>'''

'''
[Before the database commit](https://github.com/hanhanhan/robot_rkelly/blob/master/app/main/views.py#L79):
None Title <class 'NoneType'>
127.0.0.1 - - [23/Feb/2017 14:02:59] "GET /song-lyrics/ HTTP/1.1" 302 -
'''
linked_lyrics route song title:  None
'''
Update requirements
Add favicon for tab
Add github/about, facebook, twitter linking
Add facebook header info
Add db of created songs
Add glitch effect
Different sized screens layouts
Custom error pages
Nginx for static resources

Add title
xCapitalization on line

margin/padding below lyrics?
