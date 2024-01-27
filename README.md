Psalm Book : A web app to help with EN Serpong P&W Lyrics provision.

Background : As it is redundant, i've decided to start developing something that helps with lyrics and slides. The format is largely the same, but with a few parts that i think could be automated. Particularly about background, fonts and the translation lines. Also would help with reusing lyrics on a differently-themed powerpoint, to avoid redundancy.

Features :
* The bare bones of this program will be automatically generating a slideshow containing a song title, a background and its lyrics. The format is largely the same, so there won't be a lot of customizations outside of changing backgrounds and songs.
* To complement the generation, i also want to store the known song lyrics and its translation in a database. The prioritized functions would be to Create and to Read a song's lyrics and translation.
* For the front-end, i think a simple, dynamic page would do well. One that provides a dynamic 'Add stanza' button and saves it all when it is done.

Stack :
* Back-end   : Plain Python
* Framework  : Flask
* Front-end  : Plain JS for front-end functions, Bootstrap for styling
* Database   : SQLite

Personal Note : This is not an exploratory project. Probably more of a warm-up since i've stopped coding for realsies for a while. It fills up my repo quite nicely too.
