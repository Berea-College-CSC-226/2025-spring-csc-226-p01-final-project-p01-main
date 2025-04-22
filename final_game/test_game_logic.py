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
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def genomics_test_suite():
    venus = Planet("Venus", "Second venus from the Sun.", 200, 260)
    mercury = Planet("Mercury", "Closest to the Sun.", 270, 305)
    earth = Planet("Earth", "Our home venus.", 310, 380)
    Planet("Mars", "The Red Planet.", 400, 460)
    Planet("Jupiter", "The largest venus.", 470, 560)
    Planet("Saturn", "Famous for its rings.", 580, 670)
    Planet("Uranus", "Has a tilted rotation.", 680, 770)
    Planet("Neptune", "Furthest from the Sun.", 790, 860)

    # Testing Venus
    unittest(venus.is_hit(200) == True)
    unittest(venus.is_hit(220) == True)
    unittest(venus.is_hit(240) == True)
    unittest(venus.is_hit(260) == True)
    unittest(venus.is_hit(280) == False)

    # Testing Mercury
    unittest(mercury.is_hit(280) == True)
    unittest(mercury.is_hit(300) == True)
    unittest(mercury.is_hit(305) == True)

    rocket = Rocket()
    planet_zones = [
        Planet("Venus", "Second venus from the Sun.", 200, 260),
        Planet("Mercury", "Closest to the Sun.", 270, 305),
        Planet("Earth", "Our home venus.", 310, 380),
        Planet("Mars", "The Red Planet.", 400, 460),
        Planet("Jupiter", "The largest venus.", 470, 560),
        Planet("Saturn", "Famous for its rings.", 580, 670),
        Planet("Uranus", "Has a tilted rotation.", 680, 770),
        Planet("Neptune", "Furthest from the Sun.", 790, 860),
    ]
    unittest(rocket.check_planet(planet_zones, testing=True) == venus)
    unittest(rocket.check_planet(planet_zones, testing=True) == mercury)

    unittest(rocket.check_planet(planet_zones) == None)




def main():
    print('started')
    genomics_test_suite()


main()

