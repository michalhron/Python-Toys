#import modules
import simplegui
import random

#define global variables
gender = "Male"
month = 10
year = 1993
day = 20
before_slash = "------"
after_slash = "----"
rc = before_slash + "/" + after_slash

#helper functions
def init():
    generate()

def rcCheck(x):
    """
    Takes the rodne cislo and returns string with description evaluating
    the validity of the number
    """
    if x % 11 == 0:
        return "Valid"
    elif x % 11 != 0:
        return "Invalid"
    else:
        raise ValueError

def generate():
    """
    Takes gender, month, year and date
    and returns a possible RC
    """
    global gender, month, year, day, before_slash, after_slash, rc, possibilities

    if len(str(year)) == 4:
        year = str(year)[2:]
    before_slash = str(year) + str(month) + str(day)
    for i in range (1000):
        prov_after_slash = random.randint(1000,9999)
        try:
            if int(before_slash +  str(prov_after_slash)) % 11 == 0:
                after_slash = str(prov_after_slash)
            else:
                rc = "Error while generating, try again"
        except:
            print "Value Error"
    rc = before_slash + "/" + after_slash

def setDate(date_inp):
    global day
    try:
        if int(date_inp) < 32 and int(date_inp) > 0:
            day = date_inp
            generate()
    except:
        raise ValueError


def setMonth(month_inp):
    global month
    if int(month_inp) < 13 and int(month_inp) > 0:
        month = month_inp
        generate()
    else:
        print "wrong input"

def setYear(year_inp):
    global year
    if str(year) > 1:
        if year_inp < 100:
            year = year_inp
            generate()
        if year_inp>1000:
            year = str(year_inp)[2:4]
            generate()
        else:
            print "Wrong input"


def setGender():
    global month, gender
    if month < 50:
        month = int(month) + 50
        gender = "Female"
        generate()
    elif month > 50:
        month = int(month) - 50
        gender = "Male"
        generate()



# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(rc, [30,112], 48, "White", "sans-serif")
    canvas.draw_text("Month: " + str(month), [30,184], 24, "Gray", "sans-serif")
    canvas.draw_text("Date: " + str(day), [30,160], 24, "Gray", "sans-serif")
    canvas.draw_text("Year: " + str(year), [30,208], 24, "Gray", "sans-serif")
    canvas.draw_text("Gender: " + gender, [30,232], 24, "Gray", "sans-serif")




# Create a frame
frame = simplegui.create_frame("Home", 400, 300)

#control items registration
date_inp = frame.add_input('Set Date', setDate, 20)
month_inp = frame.add_input('Set Month', setMonth, 20)
year_inp = frame.add_input('Set Year', setYear, 20)
gernder_inp = frame.add_button('Gender', setGender, 40)
frame.add_button("Generate", generate)



frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
