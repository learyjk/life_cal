thelifecal is my interpretation of "Your Life in Weeks" by Tim Urban.
https://waitbutwhy.com/2014/05/life-weeks.html

thelifecal will motivate you.  We only have so much time for this world,
and the clock never stops ticking.

thelifecal uses Django and Postgres for my CS50 Web final project.
A live version of the site can be viewed here:
http://thelifecal.com

User must first register and provide a birthday.  From there,
A Postgres Week object is built for each work in that person's
life assuming an 85 year lifespan.  After logging in, a user
will see rows of X's and O's.  X's represent a week that has
already occurred, while an O represents a future week.  The
current week is marked with an H.

From here, a user can click on individual weeks and add highlights.
In this way, life-cal also acts as a life journal.

thelifecal can be viewed on both large and small screens.  For
large screens (>1200px) each row will contain 52 weeks (1 year).
For small screens (<1200px) each row will be 13 weeks (1 quarter).
This was a design choice to keep the calendar mobile responsive
and maintain a clean-looking design while displaying a lot of
characters.

Users can also delete week highlights.

Database model schema:
Week - Holds data on each individual week.
Note - Holds highlights (note) and refers (ForeignKey) to a Week.
User - Django default
Profile - Holds birthdate info because Django default User doesn't.

Most people react to this project by saying "There's too many Xs!"
I hope it can be a motivating tool to get our there and achieve
your dreams!

Future Improvements:
1. Styling the calendar based on stages of life or highlights.
i.e. color weeks that make up childhood, school, college, career,
etc. Color weeks that have highlights to make them easy to find.
Color weeks that have your birthdate! (Not always the first week).

2. Allow user to change his/her life expectancy.  This would allow
users older than 85 to use the life-cal! Would be a good exercise
in database management too.

3. Make the calendar printable so you can hang it on your fridge!
Right now printing isn't too pretty.
