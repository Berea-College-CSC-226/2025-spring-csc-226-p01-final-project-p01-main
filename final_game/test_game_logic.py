from inspect import getframeinfo, stack
from finalcode import Planet, Rocket

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def rocket_game_test_suite():
    # Setup test planets (with image names)
    venus = Planet("Venus", "Second planet from the Sun.", 200, 260, "venus.jpg")
    mercury = Planet("Mercury", "Closest planet to the Sun.", 300, 360, "mercury.jpg")
    planets = [venus, mercury]

    # Test Planet.is_hit()
    unittest(venus.is_hit(220) == True)  # inside Venus range
    unittest(venus.is_hit(199) == False) # outside Venus range
    unittest(mercury.is_hit(350) == True)  # inside Mercury range
    unittest(mercury.is_hit(400) == False) # outside Mercury range

    # Test Rocket movement and planet detection
    rocket = Rocket()

    # Set rocket x position to a value inside Venus zone
    rocket.x = 230
    hit_planet = rocket.check_planet(planets, testing=True)
    unittest(hit_planet == venus)

    # Set rocket x position to a value inside Mercury zone
    rocket.x = 310
    hit_planet = rocket.check_planet(planets, testing=True)
    unittest(hit_planet == mercury)

    # Set rocket x position outside any planet zone
    rocket.x = 100
    hit_planet = rocket.check_planet(planets, testing=True)
    unittest(hit_planet != venus and hit_planet != mercury)

if __name__ == "__main__":
    rocket_game_test_suite()
